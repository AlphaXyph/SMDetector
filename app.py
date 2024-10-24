from flask import Flask, request, jsonify
from flask_cors import CORS
from spam_detector import SpamDetector

app = Flask(__name__)
CORS(app)

detector = SpamDetector()

# Train your model with the chunked dataset in the dataset_chunks directory
detector.train('dataset_chunks/spam_email_dataset_*.csv')  # Load all chunked files

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    email_content = data['email']
    prediction = detector.predict(email_content)
    result = 'Spam' if prediction == 1 else 'Not Spam'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
