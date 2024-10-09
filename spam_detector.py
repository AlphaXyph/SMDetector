import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import re
import glob

class SpamDetector:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.is_first_fit = True  # Flag to track first fit

    def train(self, data_path_pattern):
        first_chunk = True  # Track if processing the first chunk

        for file in glob.glob(data_path_pattern):
            chunk = pd.read_csv(file)

            # Preprocessing text data
            chunk['text'] = chunk['text'].apply(self.clean_text)

            # Split data into features and labels
            X = chunk['text']
            y = chunk['label']

            if first_chunk:
                # Fit the vectorizer and transform the first chunk
                X_vectorized = self.vectorizer.fit_transform(X)
                self.model.fit(X_vectorized, y)  # Fit the model on the first chunk
                first_chunk = False  # Update flag to false after processing the first chunk
            else:
                # Transform the text for subsequent chunks using the already fitted vectorizer
                X_vectorized = self.vectorizer.transform(X)
                self.model.partial_fit(X_vectorized, y, classes=[0, 1])  # Specify classes explicitly

    def clean_text(self, text):
        # Simple text cleaning
        text = re.sub(r'\W', ' ', text)  # Remove special characters
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        text = text.lower()  # Convert to lowercase
        return text

    def predict(self, text):
        cleaned_text = self.clean_text(text)  # Clean the input text
        vect_text = self.vectorizer.transform([cleaned_text])  # Transform the text
        return self.model.predict(vect_text)[0]
