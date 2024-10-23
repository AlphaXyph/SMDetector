document.getElementById('checkSpam').addEventListener('click', function() {
    const emailText = document.getElementById('emailText').value;  // Get email content from textarea

    // Make a POST request to the prediction endpoint
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Set content type to JSON
        },
        body: JSON.stringify({ text: emailText })  // Sending the email text in JSON format
    })
    .then(response => response.json())  // Parse JSON response
    .then(data => {
        console.log("Prediction:", data.prediction);  // Debug log to see the prediction
        document.getElementById('result').innerText = data.prediction;  // Display prediction result
        document.getElementById('feedback').style.display = 'block';  // Show feedback options
        
        // Handle result styling
        const resultBox = document.getElementById('result');
        resultBox.classList.remove('spam', 'not-spam');  // Clear previous styles

        if (data.prediction === 'Spam') {  // Match the exact string returned
            resultBox.classList.add('spam');  // Add spam style
        } else {
            resultBox.classList.add('not-spam');  // Add not spam style
        }

        // Store prediction result for feedback
        window.predictedLabel = data.prediction === 'Spam' ? 1 : 0;  // Set label based on prediction
        window.emailText = emailText;  // Store email text for feedback
    })
    .catch((error) => {
        console.error('Error:', error);  // Log errors if any
    });
});

// Handle feedback submission for 'Yes' feedback
document.getElementById('feedbackYes').addEventListener('click', function() {
    submitFeedback(window.emailText, window.predictedLabel);  // Submit feedback with predicted label
});

// Handle feedback submission for 'No' feedback
document.getElementById('feedbackNo').addEventListener('click', function() {
    const oppositeLabel = window.predictedLabel === 1 ? 0 : 1;  // Reverse the label for feedback
    submitFeedback(window.emailText, oppositeLabel);  // Submit feedback with opposite label
});

// Function to submit feedback to the server
function submitFeedback(emailText, label) {
    fetch('http://127.0.0.1:5000/feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Set content type to JSON
        },
        body: JSON.stringify({ text: emailText, feedback: label === 1 ? "yes" : "no" })  // Send feedback as JSON
    })
    .then(() => {
        document.getElementById('feedback').style.display = 'none';  // Hide feedback section
        alert('Thank you for your feedback!');  // Thank user for feedback
    })
    .catch((error) => {
        console.error('Error:', error);  // Log errors if any
    });
}
