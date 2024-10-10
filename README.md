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
