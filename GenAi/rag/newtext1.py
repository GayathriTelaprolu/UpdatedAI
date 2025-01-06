import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sentence_transformers import SentenceTransformer
import chromadb
import os

# Initialize SBERT model and Chroma DB
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()

# Create a collection in Chroma DB
db = client.create_collection('file_chunks')

# Function to chunk the text file into paragraphs
def chunk_file(file_path):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        text = file.read()
    paragraphs = text.split('\n\n')
    return paragraphs
def chunk_file(file_path):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        text = file.read()
    paragraphs = text.split('\n\n')
    return paragraphs



# Function to embed and store chunks in Chroma DB
def store_chunks_in_db(paragraphs):
    db.delete()  # Clear existing data in the database (if any)
    for para in paragraphs:
        if para.strip():  # Avoid empty paragraphs
            embedding = model.encode(para)
            db.add(documents=[para], embeddings=[embedding])
            print(f"Stored chunk: {para[:30]}...")  # Print the first 30 characters of the chunk

# Function to monitor changes in the file
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.last_modified = os.path.getmtime(file_path)
        self.last_paragraphs = chunk_file(file_path)

    def on_modified(self, event):
        if event.src_path == self.file_path:
            current_modified = os.path.getmtime(self.file_path)
            if current_modified > self.last_modified:
                print("\nFile changed, processing the updates...")
                new_paragraphs = chunk_file(self.file_path)
                self.detect_changes(new_paragraphs)
                self.last_modified = current_modified
                self.last_paragraphs = new_paragraphs
                store_chunks_in_db(new_paragraphs)

    def detect_changes(self, new_paragraphs):
        added = [para for para in new_paragraphs if para not in self.last_paragraphs]
        removed = [para for para in self.last_paragraphs if para not in new_paragraphs]

        if added:
            for para in added:
                print(f"Paragraph inserted: {para[:30]}...")

        if removed:
            for para in removed:
                print(f"Paragraph deleted: {para[:30]}...")

# Initialize the file change handler and observer
file_path = 'C:/Users/Public/genai1/GenAi/rag/textfiles/text1.txt'
event_handler = FileChangeHandler(file_path)
observer = Observer()
observer.schedule(event_handler, os.path.dirname(file_path), recursive=False)

# Start monitoring the file for changes
observer.start()
try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    observer.stop()
observer.join()
