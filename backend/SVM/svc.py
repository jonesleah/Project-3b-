import joblib
import os
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")
nltk.download('punkt')
# Load SVC models
svc_path = os.path.join(os.path.dirname(__file__), '../SVM/svc_model.pkl')
svc_vectorizer_path = os.path.join(os.path.dirname(__file__), '../SVM/tfidf_vectorizer.pkl')
svc_model = joblib.load(svc_path)
tfidf = joblib.load(svc_vectorizer_path)


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


# Process the email and apply the SVC model
def run_svc(message):
    clean_message = process_message(message)
    message_vector = tfidf.transform([clean_message])
    classification = svc_model.predict(message_vector)[0]
    return classification
