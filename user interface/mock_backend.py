from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

print("Static Folder Path:", os.path.abspath(app.static_folder))
print("Current Working Directory:", os.getcwd())
print("Files in Static Folder:", os.listdir(os.path.abspath(app.static_folder)))

@app.route('/api/classify', methods=['POST'])
def classify():
    data = request.json
    email_content = data.get('email', '')

    # Simulate processing time
    import time
    time.sleep(2)

    # Mock classification result
    if 'spam' in email_content.lower():
        result = 'Spam'
    else:
        result = 'Not Spam'

    return jsonify({'classification': result})

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)