# Import necessary functions and modules
from src.helper import load_pdf_files, text_chunking, download_embeddings_model
from langchain.vectorstores import Pinecone
import pinecone
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve Pinecone API key and environment from environment variables
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# Load PDF files, chunk text, and download embeddings model
loaded_pdf_content = load_pdf_files("Data/")  # Load PDF files from the "Data/" directory
doc_chunks = text_chunking(loaded_pdf_content)  # Chunk the loaded PDF content into smaller segments
embeddings = download_embeddings_model()  # Download and initialize an embeddings model

# Initialize Pinecone environment and create a document search index
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)  # Initialize Pinecone with API key and environment
docsearch=Pinecone.from_texts([t.page_content for t in doc_chunks], embeddings, index_name='chatbot')  # Create a document search index named "chatbot" using embeddings