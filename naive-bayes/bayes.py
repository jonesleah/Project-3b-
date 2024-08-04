import csv
import re
import math
import random
from collections import defaultdict


def load_from_csv(path):
    data = []
    with open(path, mode='r') as csvfile:
        reader = csv.reader(csvfile)

        next(reader) #skip header row

        for row in reader:
            label, text = row # store each column in its respective variable
            data.append((label, text)) # store each row as a tuple in my array
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


def main():
    data = load_from_csv("../datasets/spam.csv")
    
    training_data, validation_data = slice_data(data, train_ratio=0.8)

    normal_train, spam_train = split(training_data)

    p_spam, p_ham, spam_word_probs, normal_word_probs = likelihoods(normal_train, spam_train)

    # Compare to validation data:
    correct_predictions = 0

    for label, email in validation_data:
        prediction = classifer(email, p_spam, p_ham, spam_word_probs, normal_word_probs)
        if prediction == label:
            correct_predictions += 1

    accuracy = correct_predictions / len(validation_data)
    print(f"Validation Accuracy: {accuracy * 100:.2f}%")



if __name__ == "__main__":
    main()