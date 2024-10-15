import pandas as pd
import os

# Load the full dataset (change the file path accordingly)
dataset_path = "spam_ham_dataset.csv"  # Replace this with your actual file path
output_folder = "dataset_chunks"  # Folder to save chunks

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the entire dataset
df = pd.read_csv(dataset_path)

# Define the chunk size (number of rows per chunk)
chunk_size = 20000  # Adjust this number depending on your file size and GitHub's 100 MB limit

# Split the DataFrame into smaller chunks
for i, chunk in enumerate(range(0, len(df), chunk_size)):
    # Select chunk
    chunk_df = df[chunk:chunk + chunk_size]

    # Define the output file name
    chunk_file = os.path.join(output_folder, f"spam_ham_chunk_{i+1}.csv")

    # Save the chunk to a CSV file
    chunk_df.to_csv(chunk_file, index=False)

    print(f"Chunk {i+1} saved: {chunk_file}")
