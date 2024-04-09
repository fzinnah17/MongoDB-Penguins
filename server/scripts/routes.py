# Create a new Flask application
# Import necessary libraries
from flask import Flask, render_template, request
from pymongo import MongoClient
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, VectorStoreIndex, StorageContext, SimpleDirectoryReader
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

mongo_uri = os.environ["MONGO_URI"]
print(mongo_uri)
app = Flask(__name__)

# Create the MongoDB client instance
mongodb_client = MongoClient(mongo_uri)

# Initialize a vector search object for the MongoDB atlas with the MongoDB client
store = MongoDBAtlasVectorSearch(mongodb_client, db_name="test-database", collection_name="uber_docs", index_name="default")
storage_context = StorageContext.from_defaults(vector_store=store)

@app.route('/Upload', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']
        # Define the path to the documents subfolder of the server folder
        file_path = os.path.join(os.getcwd(), 'server', 'documents', file.filename)
        # Save the file to the specified location
        file.save(file_path)
        # Load the data from the file
        uploaded_docs = SimpleDirectoryReader(os.path.dirname(file_path)).load_data()
        # Index the data
        index = VectorStoreIndex.from_documents(uploaded_docs, storage_context=storage_context)
        # Return a success message
        return "File uploaded and indexed successfully"
    else:
        return render_template('upload.html')

# Main function
if __name__ == '__main__':
    app.run(port=5000, debug=True)