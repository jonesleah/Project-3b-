import csv
import re
import math
import random
from collections import defaultdict

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

from sklearn.metrics import confusion_matrix
import seaborn as sns

from sklearn.metrics import roc_curve, roc_auc_score

def plot_roc_curve(labels, probabilities):
    fpr, tpr, _ = roc_curve(labels, probabilities, pos_label='spam')
    auc = roc_auc_score(labels, probabilities)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'AUC = {auc:.2f}'))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Random Classifier', line=dict(dash='dash')))

    fig.update_layout(title='ROC Curve', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
    fig.write_html('roc_curve.html')


def plot_confusion_matrix(validation_data, predictions):
    labels = [item[0] for item in validation_data]
    cm = confusion_matrix(labels, predictions, labels=['ham', 'spam'])
    
    fig = go.Figure(data=go.Heatmap(
                   z=cm,
                   x=['Predicted Ham', 'Predicted Spam'],
                   y=['Actual Ham', 'Actual Spam'],
                   hoverongaps=False))
    
    fig.update_layout(title='Confusion Matrix', xaxis_title='Predicted Label', yaxis_title='True Label')
    fig.write_html('confusion_matrix.html')


def preprocess_file(input_path, output_path):
    # Preprocess the file to remove null bytes. 
    with open(input_path, 'rb') as infile, open(output_path, 'wb') as outfile:
        # Read the entire file and replace null bytes with nothing
        content = infile.read().replace(b'\x00', b'')
        outfile.write(content)

def load_from_csv(path):
    data = []

    csv.field_size_limit(10**6)  # Set the limit to 1 MB because messages are too long

     # Preprocess the file to remove null bytes
    preprocessed_path = 'preprocessed_' + path
    preprocess_file(path, preprocessed_path)

    with open(preprocessed_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)

        header = next(reader) #skip header row
        label_idx = header.index("Spam/Ham")
        text_idx = header.index("Message")

        for row in reader:
            label = row[label_idx]
            text = row[text_idx]
            if label and text:
                data.append((label, text))
        return data

def slice_data(data, train_ratio = 0.8):
    random.shuffle(data)
    split_index = int(len(data) * train_ratio)
    train_data = data[split_index:]
    validation_data = data[:split_index]
    return train_data, validation_data

def split(data):
    normal = []
    spam = []

    for i in range(0, len(data)):
        if data[i][0] == "ham":
            normal.append(data[i][1])
        else:
            spam.append(data[i][1])
    
    return normal, spam

def tokenize(data):
    word_count = defaultdict(int)

    for i in range(len(data)):
        text = re.sub(r'[^a-zA-Z\s]','', data[i])
        words = text.lower().split()
        
        for word in words:
            word_count[word] += 1
    
    return word_count

def likelihoods(normal, spam):
    # Total num of emails:
    total_emails = len(normal) + len(spam)

    # Overall likelihood:
    spam_p = len(spam) / total_emails
    normal_p  = len(normal)  / total_emails

    # Word counts:
    spam_counts   = tokenize(spam)
    normal_counts = tokenize(normal)

    # Total word counts:
    total_spam_counts   = sum(spam_counts.values())
    total_normal_counts = sum(normal_counts.values())

    spam_words_p = {word: spam_counts[word] / total_spam_counts for word in spam_counts}
    normal_words_p = {word: normal_counts[word] / total_normal_counts for word in normal_counts}

    return spam_p, normal_p, spam_words_p, normal_words_p


def classifer(email, spam_p, normal_p, spam_words_p, normal_words_p):
    
    # Tokenize this email
    email = re.sub(r'[^a-zA-Z\s]', '', email).lower().split()

    # Logarithmic probabilities -- to ensure that the number can be accurately compared (it is a problem sometimes)
    spam_log_p = math.log(spam_p)
    normal_log_p = math.log(normal_p)

    for word in email:
        if word in spam_words_p:
            spam_log_p += math.log(spam_words_p[word])
        if word in normal_words_p:
            normal_log_p += math.log(normal_words_p[word])

    # Compare probabilities to classify:
    return "spam" if spam_log_p > normal_log_p else "ham"

def plot_word_counts(normal_counts, spam_counts):
    # Convert counts to DataFrame for better handling
    normal_df = pd.DataFrame(list(normal_counts.items()), columns=['Word', 'Count']).sort_values(by='Count', ascending=False)
    spam_df = pd.DataFrame(list(spam_counts.items()), columns=['Word', 'Count']).sort_values(by='Count', ascending=False)

    # Plot Normal Words
    fig_normal = go.Figure()
    fig_normal.add_trace(go.Bar(x=normal_df['Word'][:20], y=normal_df['Count'][:20], name='Normal'))
    fig_normal.update_layout(title='Top 20 Words in Ham Messages', xaxis_title='Word', yaxis_title='Count')

    # Plot Spam Words
    fig_spam = go.Figure()
    fig_spam.add_trace(go.Bar(x=spam_df['Word'][:20], y=spam_df['Count'][:20], name='Spam'))
    fig_spam.update_layout(title='Top 20 Words in Spam Messages', xaxis_title='Word', yaxis_title='Count')

    # Save plots to HTML
    fig_normal.write_html('normal_words.html')
    fig_spam.write_html('spam_words.html')

def plot_message_counts(data):
    # Count the number of spam and ham messages
    labels = [item[0] for item in data]
    counts = {'ham': labels.count('ham'), 'spam': labels.count('spam')}

    fig = go.Figure()
    fig.add_trace(go.Bar(x=list(counts.keys()), y=list(counts.values()), name='Messages'))
    fig.update_layout(title='Number of Spam vs Ham Messages', xaxis_title='Message Type', yaxis_title='Count')

    # Save plot to HTML
    fig.write_html('message_counts.html')

def plot_accuracy(accuracy):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=['Accuracy'], y=[accuracy], name='Accuracy'))
    fig.update_layout(title='Model Accuracy', xaxis_title='Metric', yaxis_title='Accuracy')
    fig.write_html('accuracy.html')


def main():
    data = load_from_csv("enron_spam_data.csv")
    
    training_data, validation_data = slice_data(data, train_ratio=0.8)

    normal_train, spam_train = split(training_data)

    p_spam, p_ham, spam_word_probs, normal_word_probs = likelihoods(normal_train, spam_train)

    # Compare to validation data:
    correct_predictions = 0
    predictions = []

    for label, email in validation_data:
        prediction = classifer(email, p_spam, p_ham, spam_word_probs, normal_word_probs)
        predictions.append(prediction)
        if prediction == label:
            correct_predictions += 1

    accuracy = correct_predictions / len(validation_data)
    print(f"Validation Accuracy: {accuracy * 100:.2f}%")

    # Plot and save word counts
    plot_accuracy(accuracy*100)
    plot_confusion_matrix(validation_data, predictions)
    plot_word_counts(normal_word_probs, spam_word_probs)
    plot_message_counts(data)




if __name__ == "__main__":
    main()