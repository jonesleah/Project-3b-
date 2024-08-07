## DEPLOYED SITE: [[(https://emailspamdetector-soly.onrender.com/)](https://emailspamdetector-soly.onrender.com/)]

*Render's free tier spins down with inactivity; requests may be delayed up to 50 seconds*
## PROJECT REPORT- https://docs.google.com/document/d/1jqUHO3-qHthq0iyGooUrRAs2Rn_KzHBKRuaVYPjlO0w/edit?usp=sharing

## VIDEO DEMO - https://youtu.be/xNDlM6yQIuw

### Team Name
Final Project Group 5


### Team Members
Leah Jones, Newman Waters, Serena Seymour


### Project
Email Spam Detection Using Naive Bayes and Support Vector Machines
- Classifying emails as spam or not spam using machine learning algorithms
- Spam emails are unsolicited messages that can clutter inboxes and pose security risks. Detecting
and filtering these spam emails most effectively is crucial for improving email communication
efficiency and security.


### Tools Used
- Main Language: Python
- Flask web framework for backend API
- Pycharm for data processing and algorithm development
- Jupyter Notebook to visualize the model as we train
- scikit-learn machine learning library for Python
- pandas library for DataFrame use
- NLTK for natural language processing (NLP) of the email dataset
- Basic frontend (HTML/CSS/JavaScript)
- plotly and matplotlib libraries for plotting insightful graphs on the data
  

### Running this locally
1. Ensure all dependencies are installed (in `Project-3b-/backend/requirements.txt`)
2. Navigate to `Project-3b-/backend/`
3. Run `python3 app.py`
4. Navigate to location specified by terminal (most likely http://127.0.0.1:5000) and open in browser
5. Keep program running while interacting with user interface


### Requirements:
Flask~=3.0.3

nltk~=3.8.1

scikit-learn~=1.2.2

joblib~=1.4.2

matplotlib~=3.9.0

pandas~=2.2.2

plotly~=5.23.0

numpy~=1.23.5

gunicorn
   

### Visuals: User interface
- Access the prototype Render deployment here: https://emailspamdetector-soly.onrender.com/
- PLEASE NOTE: This might run slower than shown on video! This is a free hosting service...


### How our code works
Our project is focused on spam detection using machine learning algorithms. The frontend is developed using HTML, CSS, and JavaScript to allow users to input email content for spam detection. The backend, developed with Flask, handles API requests and processes the data using Python. The primary algorithm implemented is a Naive Bayes classifier, with plans to compare its performance to a Support Vector Machine (SVM) classifier. The data for the project is sourced from the Enron email dataset, which has been preprocessed to remove noise and improve accuracy. Our system aims to classify emails as spam or not spam with high precision and efficiency.


### Example Prompts:
**Ham** (Non-Spam)

Hi! Looking forward to meeting you later today! Thanks.

Can we reschedule our meeting to tomorrow afternoon? I have a conflict with the original time and would like to discuss the project updates before the end of the week. Let me know if this works for you, and I’ll send a new calendar invite.

Do you have the latest sales report ready? We need it for the upcoming meeting with the board of directors. Make sure all the data is up-to-date and accurate. Let me know if you need any assistance with the report.

**Spam**

This is not a scam! You've been chosen to receive a $500 Amazon gift card.

You have been selected for a free iPhone 14. Claim yours by clicking this link and completing a short survey. This exclusive offer is available only to a few lucky individuals, so don't wait. Get your brand-new iPhone 14 now!

Urgent! Your account has been compromised. Verify your identity by clicking here.




### References
- https://www2.aueb.gr/users/ion/data/enron-spam/
- https://github.com/MWiechmann/enron_spam_data/raw/master/enron_spam_data.zip
