from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List


def load_pdf_files(data_directory: str) -> List[str]:
    """
    Load PDF files from a specified directory.

    Args:
        data_directory (str): The directory path containing PDF files.

    Returns:
        List[str]: A list of text content extracted from the PDF files.
    """
    # Create a DirectoryLoader instance to load PDF files
    pdf_loader = DirectoryLoader(
        data_directory,            # Specify the directory to search for PDF files
        glob="*.pdf",              # Specify the pattern for PDF files
        loader_cls=PyPDFLoader    # Use PyPDFLoader class to load PDF content
    )

    # Load PDF files and extract text content
    docs = pdf_loader.load()

    # Return the extracted text content from PDF files
    return docs

def text_chunking(loaded_pdf_content: str) -> List[str]:
    """
    Chunk the loaded PDF content into smaller segments.

    Args:
        loaded_pdf_content (str): The text content loaded from PDF files.

    Returns:
        List[str]: A list of text chunks, each representing a smaller segment of the original content.
    """
    # Initialize a RecursiveCharacterTextSplitter instance
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,          # Specify the size of each text chunk
        chunk_overlap=20         # Specify the overlap between adjacent chunks
    )

    # Split the loaded PDF content into smaller segments (chunks)
    chunks = splitter.split_documents(loaded_pdf_content)

    # Return the list of text chunks
    return chunks

def download_embeddings_model() -> HuggingFaceEmbeddings:
    """
    Download and initialize the embeddings model.

    Returns:
        HuggingFaceEmbeddings: An instance of the embeddings model.
    """
    # Initialize the HuggingFaceEmbeddings instance with the specified model name
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    # Return the initialized embeddings model
    return embeddings