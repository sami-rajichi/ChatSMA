from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings_model
from langchain.vectorstores import Pinecone
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Retrieve Pinecone API key and environment from environment variables
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# Download embeddings model
embeddings = download_embeddings_model()

# Initialize Pinecone with API key and environment
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)

# Define the name of the index for Pinecone
index_name = "chatbot"

# Create Pinecone index searcher
docsearch = Pinecone.from_existing_index(index_name, embeddings)

# Define the prompt template for the chatbot
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Define chain type arguments for the model
chain_type_kwargs = {"prompt": PROMPT}

# Load LLM model for conversational AI
llm = CTransformers(model="Model\llama-2-7b-chat.ggmlv3.q8_0.bin",
                    model_type="llama",
                    config={'max_new_tokens': 512,
                            'temperature': 0.8})

# Initialize Retrieval QA chain for conversational QA
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 3}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

@app.route("/")
def index():
    """Render the index page"""
    return render_template('chatbot.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    """Handle chat interactions"""
    # Get the message from the request
    msg = request.args.get('msg')
    input = msg
    # Get response from QA model
    result = qa({"query": input})
    print("Response : ", result["result"])
    # Return the result as string
    return str(result["result"])

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)