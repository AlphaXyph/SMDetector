import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import re
import glob

class SpamDetector:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train(self, data_path_pattern):
        # Load and process all chunks matching the pattern
        for file in glob.glob(data_path_pattern):
            self.process_chunk(pd.read_csv(file))

    def process_chunk(self, chunk):
        # Preprocessing text data
        chunk['text'] = chunk['text'].apply(self.clean_text)

        # Split data into features and labels
        X = chunk['text']
        y = chunk['label']

        # Fit the vectorizer and transform the text
        X_vectorized = self.vectorizer.fit_transform(X)

        # Train the model (you might want to append to existing data)
        self.model.partial_fit(X_vectorized, y)

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
