# Spam Email Detector Chrome Extension

## Overview
The **Spam Email Detector** is a Chrome extension that allows users to detect whether an email is spam or not by using a trained machine learning model. The model is hosted on a Flask server deployed via Render and can classify an email as "Spam" or "Not Spam" based on the content.

### Demo
You can access the backend API at: [SMDetector on Render](https://smdetector.onrender.com)

## Features
- **Spam Detection**: Quickly determine if an email is spam or not.
- **Lightweight Extension**: Simply paste email text into the extension and get results.
- **Real-time API**: Sends the email content to a Flask backend hosted on Render, which classifies the email using a Naive Bayes model.
- **Modern Chrome Extension**: Built with Manifest Version 3.

## How It Works
1. **Enter the Email Content**: Paste the email body into the extension popup.
2. **Spam Check**: The extension sends the email text to the backend API hosted on Render.
3. **Get Results**: The server returns whether the email is spam or not, and the extension displays the result.

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/AlphaXyph/SMDetector.git

2. Open Google Chrome and navigate to chrome://extensions/.

3. Enable Developer Mode (toggle in the top right corner).

4. Click on "Load Unpacked" and select the folder where you downloaded/cloned this repository.

5. The Spam Email Detector extension should now be loaded into Chrome.

## Usage
6. Click on the Spam Email Detector extension icon in your Chrome toolbar.
7. A popup will appear with a textarea.
8. Paste the email content you want to check.
9. Press Check if Spam.
10. The result will be displayed (either "This is SPAM" or "This is NOT SPAM").

## Test Cases

The following are some test cases used to evaluate the Spam Email Detector. These are example email contents along with the expected results (whether the email is Spam - 1 or Not Spam - 0).

| **Email Text**                                                                                                | **Expected Label** |
|---------------------------------------------------------------------------------------------------------------|--------------------|
| "Hey, how are you doing? Just wanted to check in and say hello."                                                | 0                  |
| "Congratulations! You've won a prize. Click here to claim your reward: http://malicious-site.com"               | 1                  |
| "Good morning, looking forward to our meeting next week. Best regards, John"                                   | 0                  |
| "You have an unclaimed reward waiting. Urgent! Update your account here: http://fake-bank-login.com"            | 1                  |
| "Hi, we noticed unusual activity on your account. Click here to secure it: http://malicious-site.com"           | 1                  |
| "Hello, I wanted to remind you about the project deadline. Let's catch up soon."                               | 0                  |
| "You've won a free gift card with your next purchase! Click here to redeem: http://fraud-site.biz"              | 1                  |
| "Hey, long time no see! Let's grab lunch this weekend if you're free."                                         | 0                  |
| "Important! Your account has been compromised. Please update your information now: http://phishing-link.co"     | 1                  |
| "Hi, please review the attached contract and let me know your feedback. Thank you."                            | 0                  |
| "Limited time offer! Get rich quick by investing in this one simple trick. Act fast!"                          | 1                  |
| "Hey, I just wanted to share this amazing opportunity with you. Click here for more details: http://spam-link" | 1                  |
| "Hello, your invoice for last month is overdue. Please pay here: http://legitimate-payment.com"                 | 0                  |
| "Hi, don't miss out on this once-in-a-lifetime opportunity! Click here for more info: http://spam-site.com"    | 1                  |
| "Just a quick follow-up on our conversation. Let me know if you need anything."                                | 0                  |

