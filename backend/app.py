from flask import Flask, request, jsonify, send_from_directory
import os
from SVM.svc import run_svc
from NB.nb import run_nb

app = Flask(__name__, static_folder='../frontend')

print("Static Folder Path:", os.path.abspath(app.static_folder))
print("Current Working Directory:", os.getcwd())
print("Files in Static Folder:", os.listdir(os.path.abspath(app.static_folder)))


@app.route('/api/classify', methods=['POST'])
def classify():
    data = request.json
    email_content = data.get('email', '')

    # Call both classifiers and print each result
    svc_result = run_svc(email_content)
    nb_result = run_nb(email_content)

    results = {
        'SVC Classification': 'Spam' if svc_result == 1 else 'Not Spam',
        'Naive Bayes Classification': 'Spam' if nb_result == 1 else 'Not Spam'
    }

    return jsonify(results)


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == '__main__':
    app.run(debug=True)
