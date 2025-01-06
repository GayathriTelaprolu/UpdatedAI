import pdfplumber
import nltk
import spacy
from nltk.tokenize import word_tokenize, sent_tokenize
import re

# Load spaCy model for sentence chunking

# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()  # Extract text from each page
    return text

# 1. Data Preprocessing Function
def preprocess_text(text):
    # Lowercasing
    text = text.lower()
    
    # Removing special characters and extra spaces
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    
    return text

# 2. Fixed-Length Chunking
def fixed_length_chunking(text, chunk_size=100):
    words = word_tokenize(text)  # Tokenize text into words
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    return [' '.join(chunk) for chunk in chunks]

# 3. Sentence-based Chunking
def sentence_based_chunking(text):
    sentences = sent_tokenize(text)  # Tokenize text into sentences
    return sentences

# 4. Sliding Window Chunking
def sliding_window_chunking(text, window_size=100, step_size=50):
    words = word_tokenize(text)
    chunks = []
    for i in range(0, len(words) - window_size + 1, step_size):
        chunks.append(' '.join(words[i:i + window_size]))
    return chunks



# Main function to extract text and perform chunking
def chunk_pdf(pdf_path):
    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Preprocess the extracted text
    processed_text = preprocess_text(extracted_text)
    
    # Perform different chunking methods
    fixed_chunks = fixed_length_chunking(processed_text, chunk_size=50)  # 50 words per chunk
    sentence_chunks = sentence_based_chunking(processed_text)
    sliding_chunks = sliding_window_chunking(processed_text, window_size=50, step_size=25)  # 50 words per chunk with step size of 25
   
    
    # Display results (you can modify this to save or further process the chunks)
    print("Fixed-Length Chunking:")
    print(fixed_chunks[:2])  # Display first 2 chunks for example
    print("\nSentence-Based Chunking:")
    print(sentence_chunks[:2])  # Display first 2 sentences
    print("\nSliding Window Chunking:")
    print(sliding_chunks[:2])  # Display first 2 sliding chunks
    

# Example PDF path
pdf_path = "sample.pdf"  # Provide the path to your PDF file
chunk_pdf(pdf_path)
