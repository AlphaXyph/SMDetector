from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from spam_detector import SpamDetector
import os
import csv

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
detector = SpamDetector()

# Load dataset and train the model
detector.train('dataset_chunks/spam_email_dataset_*.csv')  # Load all chunked files

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')  # Change from 'email' to 'text' for consistency
    
    prediction = detector.predict(text)
    return jsonify({'prediction': 'Spam' if prediction == 1 else 'Not Spam'})  # Updated output

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    user_text = data.get('text', '')
    user_feedback = data.get('feedback', '')  # Expecting 'yes' or 'no'

    # Automatically label feedback based on user input
    label = 1 if user_feedback == "yes" else 0  # 1 for spam, 0 for not spam

    # Write feedback to CSV safely
    feedback_file = 'feedback.csv'
    with open(feedback_file, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['label', 'text']  # Ensure correct order
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if file is empty to write header
        if os.stat(feedback_file).st_size == 0:
            writer.writeheader()

        # Write the feedback
        writer.writerow({'text': user_text, 'label': label})

    return jsonify({'message': 'Feedback recorded'})

@app.route('/retrain', methods=['POST'])
def retrain():
    # Retrain the model including feedback
    detector.train('dataset_chunks/spam_email_dataset_*.csv')  # Load all chunked files again
    return jsonify({'message': 'Model retrained successfully'})

if __name__ == '__main__':
    app.run(debug=True)
