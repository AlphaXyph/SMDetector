document.getElementById('checkSpam').addEventListener('click', function() {
    const emailText = document.getElementById('emailText').value;

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: emailText })  // Using 'text' instead of 'email'
    })
    .then(response => response.json())
    .then(data => {
        console.log("Prediction:", data.prediction);  // Debug log to see the prediction
        document.getElementById('result').innerText = data.prediction;  // Get the prediction from the response
        document.getElementById('feedback').style.display = 'block';  // Show feedback options
        
        // Handle result styling
        const resultBox = document.getElementById('result');
        resultBox.classList.remove('spam', 'not-spam');  // Clear previous classes

        if (data.prediction === 'Spam') {  // Match the exact string returned
            resultBox.classList.add('spam'); // Add spam class
        } else {
            resultBox.classList.add('not-spam'); // Add not spam class
        }

        // Store prediction result for feedback
        window.predictedLabel = data.prediction === 'Spam' ? 1 : 0;  // Change to match new labels
        window.emailText = emailText;  // Store email for feedback
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

// Handle feedback submission
document.getElementById('feedbackYes').addEventListener('click', function() {
    submitFeedback(window.emailText, window.predictedLabel);
});

document.getElementById('feedbackNo').addEventListener('click', function() {
    const oppositeLabel = window.predictedLabel === 1 ? 0 : 1;  // Reverse the label
    submitFeedback(window.emailText, oppositeLabel);
});

function submitFeedback(emailText, label) {
    fetch('http://127.0.0.1:5000/feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: emailText, feedback: label === 1 ? "yes" : "no" })  // Send feedback
    })
    .then(() => {
        document.getElementById('feedback').style.display = 'none';  // Hide feedback
        alert('Thank you for your feedback!');
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
