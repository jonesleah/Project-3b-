import csv
import re
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

def main():
    data = load_from_csv("../datasets/spam.csv")
    
    normal, spam = split(data)

    spam_words = tokenize(spam)
    normal_words = tokenize(normal)

    print("Spam words: " , dict(list(spam_words.items())[:100]))
    print("Normal words: ", dict(list(normal_words.items())[:100]))


if __name__ == "__main__":
    main()