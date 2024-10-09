import pandas as pd
import os

def split_dataset(input_file, chunk_size, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the dataset
    df = pd.read_csv(input_file)

    # Calculate the number of chunks
    num_chunks = len(df) // chunk_size + (len(df) % chunk_size > 0)

    # Split and save each chunk
    for i in range(num_chunks):
        chunk = df[i * chunk_size: (i + 1) * chunk_size]
        chunk_file_name = os.path.join(output_dir, f'spam_ham_chunk_{i + 1}.csv')
        chunk.to_csv(chunk_file_name, index=False)

if __name__ == "__main__":
    split_dataset('spam_ham_dataset.csv', chunk_size=10000, output_dir='dataset_chunks')  # Adjust chunk size as needed
