import csv
import string
import re


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
    all_words = []

    for i in range(len(data)):
        text = re.sub(r'[^a-zA-Z\s]','', data[i])
        words = text.lower().split()
        all_words.extend(words)
    
    return all_words

def main():
    data = load_from_csv("../datasets/spam.csv")
    
    normal, spam = split(data)

    spam_words = tokenize(spam)
    normal_words = tokenize(normal)

    print("Spam words: " ,spam_words[:1000])
    print("Normal words: ", normal_words[:1000])


if __name__ == "__main__":
    main()