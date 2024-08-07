import joblib
import os
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
nltk.download("stopwords")

# Load NB Model:
nb_path = os.path.join(os.path.dirname(__file__), "../NB/nb_model.pkl")
nb_vectorizer_path = os.path.join(os.path.dirname(__file__), "../NB/count_vectorizer.pkl")
nb_model = joblib.load(nb_path)
vectorizer = joblib.load(nb_vectorizer_path)


# Message processor:
def process_message(message):
    message = message.lower()
    message = word_tokenize(message)
    message = [word.strip() for word in message]
    message = [word.replace("\n", "") for word in message]
    message = [re.sub(r"\d+", "", word) for word in message]
    message = [re.sub(r"[^a-zA-Z0-9\s]", "", word) for word in message]
    stop_words = set(stopwords.words("english"))
    message = [word for word in message if word not in stop_words]
    ps = PorterStemmer()
    message = [ps.stem(word) for word in message]
    return " ".join(message)


# Process email and run through model
def run_nb(message):
    processed_message = process_message(message)
    message_vector = vectorizer.transform([processed_message])
    classified = nb_model.predict(message_vector)[0]
    if (classified == "spam"):
        classified = 1
    else:
        classified = 0
        
    return classified
