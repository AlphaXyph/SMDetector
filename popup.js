document.getElementById('checkSpam').addEventListener('click', function() {
    const emailText = document.getElementById('emailText').value;

    fetch('https://smdetector.onrender.com/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: emailText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.result;
        // Add class based on spam/not spam
        if (data.result === 'Spam') {
            document.getElementById('result').classList.add('spam');
            document.getElementById('result').classList.remove('not-spam');
        } else {
            document.getElementById('result').classList.add('not-spam');
            document.getElementById('result').classList.remove('spam');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
