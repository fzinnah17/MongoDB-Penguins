# check the raw data that was loaded
#print("Loaded Uber Docs:")
#print(uber_docs)  --> uncomment this if you want to see the raw data that was loaded
# provide URI to constructor, or use environment variable

from readline import redisplay  # the display() function is most likely only available to jupyter notebook
from markdown import Markdown   # TODO: There;s an issue with the import that needs fixing
import pymongo
import certifi
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.core import SimpleDirectoryReader
from llama_index.core import Response
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.nomic import NomicEmbedding
from dotenv import load_dotenv
#from transformers import LlamaForCausalLM, LlamaTokenizer
from transformers import LlamaForCausallLM, CodeLlamaTokenizer

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import Settings

import os

import torch

llm = HuggingFaceLLM(
    context_window=2048,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.25, "do_sample": False},
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="Writer/camel-5b-hf",
    model_name="Writer/camel-5b-hf",
    device_map="auto",
    tokenizer_kwargs={"max_length": 2048},
    # uncomment this if using CUDA to reduce memory usage
    # model_kwargs={"torch_dtype": torch.float16}
)

Settings.chunk_size = 512
Settings.llm = llm




# this is based on the mongoDB vector database tutorial from the documentation ot get a better understanding of how vector datbases works
# load the environment variables
load_dotenv()


#TODO: instead of huggingface, try using OpenAI model isntead
# Perform the relevant configuration to the default llama-index settings


'''
Settings.embed_model = HuggingFaceEmbedding(
    model_name="nomic-ai/nomic-embed-text-v1.5"
)
'''

nomic_api = os.getenv('NOMIC_API_KEY')
print(nomic_api)
# define the embedding model
embed_model = NomicEmbedding(api_key=nomic_api,
                             dimensionality=768,
                             model_name="nomic-embed-text-v1.5")

tokenizer = CodeLlamaTokenizer.from_pretrained("codellama/CodeLlama-7b-hf")
model = LlamaForCausallLM.from_pretrained("codellama/CodeLlama-7b-hf")

llm = model
Settings.llm = llm
Settings.embed_model = embed_model


#ollama
#Settings.llm = Ollama(model="mistral", request_timeout=30.0)

mongo_uri = os.getenv("MONGO_URI")
#openai_key = os.getenv("OPENAI_API_KEY")

mongodb_client = pymongo.MongoClient(mongo_uri, tlsCAFile=certifi.where())

#print("Mongo URI: ", mongo_uri)
#print(mongo_uri)  # print it out to see if the mongo_uri is set correctly --> test passed
#print("Open AI:", openai_key)  # print it out to see if the openai_key is set correctly --> test passed

# create the mongodb client instance
# create a mongoDB client instance by passing the connection string
# mongodb_client = pymongo.MongoClient(mongo_uri)

# embed_model = OpenAIEmbedding(embed_batch_size=10)  # note that since we changed the embedding model that we are working with, we will also need to adjust the index dimensionality
#Settings.embed_model = embed_model

# check if connection is successful or not
if mongodb_client:
    print("Successfull Connection to MongoDB Atlas")
else:
    print("Connection to MongoDB Atlas Failed")

# intialize a vector search object for the MongoDB atlas with the MongoDB client
store = MongoDBAtlasVectorSearch(mongodb_client, db_name="test-database", collection_name="nomic-docs", index_name="nomic-default")
storage_context = StorageContext.from_defaults(vector_store=store)
# nomic-docs = SimpleDirectoryReader("/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/Ayan/").load_data()

# Farnaz: Define the path to the documents subfolder of the server folder
docs_path = os.path.join(os.path.dirname(os.getcwd()), 'documents')

# Farnaz: Load the data from the documents subfolder
docs = SimpleDirectoryReader(docs_path).load_data()

# Farnaz: Print the number of documents loaded
print(f"Loaded {len(docs)} documents from {docs_path}")

# Farnaz: Index the data
index = VectorStoreIndex.from_documents(docs, storage_context=storage_context)




# check the raw data that was loaded
#print("Loaded Uber Docs:")
#print(uber_docs)  --> uncomment this if you want to see the raw data that was loaded

# index = VectorStoreIndex.from_documents(
#     nomic-docs, storage_context=storage_context
# )

# print a confirmation message to indicate that the data has been indexed
print("Indexed Data")

#about the number of documents indexed or other metadata
print(index)

# Initial Size
print("Initial Vector Store Size:")
print(store._collection.count_documents({}))  # output: 2070
# get a ref_doc_id

query="Based on the vector database information, generate a cover letter for me for the following position at Apple:\nSummary\nPosted: Feb 6, 2024\nWeekly Hours: 40\nRole Number:200518445\nAI represents a huge opportunity to elevate Apple’s products and experiences for billions of people globally. Apple is looking for Machine-Learning engineers with a background in Machine Learning, Conversational and Generative AI! You will be leveraging innovative models to build applications on top of Apple’s most advanced technologies. \nAs a Software Engineer focused on rapid prototyping of ML models, you will be responsible for designing and implementing innovative AI models and algorithms. You will work closely with other researchers and engineers to prototype and test new ideas, and collaborate with cross-functional teams to bring your research to life.\nThis role will play a critical part in helping Apple change the way humans learn about learning. You will have the opportunity to work on cutting-edge technologies that are designed to enhance human learning experiences. You will be working with a team of passionate and talented engineers and researchers who are dedicated to making a positive impact on the world through education and technology."
response = index.as_query_engine().query(query)
print("Prompt Query:", query)
#print("successful connection")
print(response)   # output: empty response

'''

When it comes to LLMS, if we want to create a proper response, we need to create a vector index within mongoDB itself

- Reference for creating mbedding can be found here: https://www.mongodb.com/docs/atlas/atlas-search/field-types/knn-vector/
'''
#redisplay(Markdown(f"<b>{response}</b>"))
# Get a ref_doc_id

'''  --> running the code below causes the following error : IndexError: list index out of range
typed_response = (
    response if isinstance(response, Response) else response.get_response()
)
ref_doc_id = typed_response.source_nodes[0].node.ref_doc_id
print(store._collection.count_documents({"metadata.ref_doc_id": ref_doc_id}))
# Test store delete
if ref_doc_id:
    store.delete(ref_doc_id)
    print(store._collection.count_documents({}))


index:
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "embedding": {
        "dimensions": 384,
        "similarity": "euclidean",
        "type": "knnVector"
      }
    }
  }
}

'''