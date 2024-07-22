### Team Name
Final Project Group 5


### Team Members
Leah Jones, Newman Waters, Serena Seymour


### Project Title
Email Spam Detection Using Naive Bayes and Support Vector Machines


### Problem: What problem are we trying to solve?
- Spam Detection; classifying emails as spam or not spam using machine learning algorithms
- Spam emails are unsolicited messages that can clutter inboxes and pose security risks. Detecting
and filtering these spam emails most effectively is crucial for improving email communication
efficiency and security.


### Motivation: Why is this a problem?
- Spam detection can enhance email security and user productivity
- Spam emails can lead to phishing attacks, spread malware, and consume valuable time and
resources. An efficient spam detection system can mitigate these risks, enhance user experience,
and improve overall email security.


### Features: When do we know that we have solved the problem?
- For spam detection, success means high accuracy in classifying emails correctly. We will
compare the output of our program (spam/not spam) to the number of spam/not spam emails in
the dataset and ensure our program is at least 90% accurate and 90% precise.
- Our algorithm can accurately classify emails as spam or not spam with high precision,
maintaining a low false positive and false negative rate. The system should be able to handle a
large volume of emails efficiently and provide clear results.


### Data: Public data set we will be using and the link to the public data set
- Spam Detection: The Enron email dataset for spam detection
(https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/suggestions?status=pending&y
ourSuggestions=true)


### Tools: Programming languages or any tools/frameworks we will be using
- Main Language: Python. Flask web framework for backend API
- Pycharm for data processing and algorithm development. Jupyter Notebook to visualize the
model as we train.
- scikit-learn machine learning library for Python
- pandas library for DataFrame use
- NLTK for natural language processing (NLP) of the email dataset
- Basic frontend (HTML/CSS/JavaScript)
- Deploy application on a platform like Heroku


### Visuals: Wireframes Links to an external site. /Sketches of the interface or the menu driven program
Access the visuals server here http://127.0.0.1:5000


### Strategy: Preliminary algorithms or data structures you may want to implement
- Spam Detection; Compare Naive Bayes classifier with Support Vector Machines
- Naive Bayes Classifier: A probabilistic classifier based on applying Bayes' theorem with strong
(naive) independence assumptions.
- Support Vector Machine (SVM): A supervised learning algorithm that can classify data by finding
the optimal hyperplane that separates different classes.
- pandas DataFrame with processed email content and spam classification
- scikit-learn objects to represent the trained model and make estimations


### Distribution of Responsibility and Roles: Who is responsible for what?

- **Leah:** Data collection and cleaning/preprocessing, create backend API with Flask, deploy with Heroku
- **Serena:** Frontend development with text box for users to input email content
- **Newman:** Algorithm development with Bayes classifier
- **Collaborative:** Machine learning model training


### References
1. https://www.cs.cmu.edu/~enron/
2. https://snap.stanford.edu/data/email-Enron.html
3. https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c
4. https://www.ibm.com/topics/support-vector-machine
5. https://towardsdatascience.com/email-spam-detection-1-2-b0e06a5c0472
6. https://ieeexplore.ieee.org/document/10170187
