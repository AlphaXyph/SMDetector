import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import re
import glob
import os

class SpamDetector:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.feedback_file = 'feedback.csv'  # Path to the feedback file

        # Create feedback.csv if it doesn't exist with the correct column order
        if not os.path.exists(self.feedback_file):
            pd.DataFrame(columns=['label', 'text']).to_csv(self.feedback_file, index=False)  # Ensure correct order

    def train(self, data_path_pattern):
        # Load chunked dataset
        all_chunks = []
        for file in glob.glob(data_path_pattern):
            chunk = pd.read_csv(file)
            chunk['text'] = chunk['text'].apply(self.clean_text)
            all_chunks.append(chunk)
        
        # Concatenate all chunks into a single DataFrame
        full_data = pd.concat(all_chunks, ignore_index=True)

        # Load feedback data from CSV
        feedback_df = pd.read_csv(self.feedback_file)
        if not feedback_df.empty:
            feedback_df['text'] = feedback_df['text'].apply(self.clean_text)
            # Ensure the order of columns is consistent with the training data
            feedback_df = feedback_df[['label', 'text']]
            full_data = pd.concat([full_data, feedback_df], ignore_index=True)

        # Check if full_data is empty before training
        if full_data.empty:
            print("No training data available. Please ensure there is data in the dataset and feedback files.")
            return

        X = full_data['text']
        y = full_data['label']

        # Vectorize and fit the model
        X_vectorized = self.vectorizer.fit_transform(X)
        self.model.fit(X_vectorized, y)

    def save_feedback(self, text, label):
        # Append new feedback to feedback.csv
        feedback_df = pd.read_csv(self.feedback_file)
        new_feedback = pd.DataFrame({'label': [label], 'text': [text]})  # Ensure correct order
        updated_feedback_df = pd.concat([feedback_df, new_feedback], ignore_index=True)
        updated_feedback_df.to_csv(self.feedback_file, index=False, quoting=1)  # Use quoting to handle commas

    def clean_text(self, text):
        text = re.sub(r'\W', ' ', text)  # Remove non-word characters
        text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
        return text.lower()

    def predict(self, text):
        cleaned_text = self.clean_text(text)
        vect_text = self.vectorizer.transform([cleaned_text])
        return self.model.predict(vect_text)[0]
