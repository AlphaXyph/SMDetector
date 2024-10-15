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

The following are some test cases used to evaluate the Spam Email Detector. These are example email contents along with the expected results (whether the email is Spam or Not Spam).

| Email Content                                                                                     | Expected Result |
|---------------------------------------------------------------------------------------------------|-----------------|
| "Congratulations! You've won a $1000 Walmart gift card. Click here to claim your prize!"          | Spam            |
| "Urgent: Please update your password immediately to keep your account secure."                    | Spam            |
| "Hey, just wanted to check in on you. How have you been?"                                         | Not Spam        |
| "Act now! Limited time offer on exclusive products just for you!"                                 | Spam            |
| "Your invoice for last month is attached. Please let us know if you have any questions."          | Not Spam        |
| "FREE trial of our premium service! Sign up now!"                                                 | Spam            |
| "Reminder: Your appointment is scheduled for tomorrow at 3 PM."                                   | Not Spam        |
| "You have been selected to participate in our market research. Click the link to start!"          | Spam            |
| "Thank you for your recent purchase! Here are your order details."                                | Not Spam        |
| "Don't miss out! Join millions of people who have already signed up for our newsletter!"          | Spam            |
| "I need your help urgently! Can you please call me back as soon as you see this?"                 | Not Spam        |
| "You've received a new message from your bank. Please click here to view it."                     | Spam            |
| "Your feedback is important to us. Please take a moment to complete this short survey."           | Not Spam        |
| "Important: Changes to your account have been made. Please log in to review them."                | Spam            |
| "Can we reschedule our meeting? Let me know what works for you."                                  | Not Spam        |

