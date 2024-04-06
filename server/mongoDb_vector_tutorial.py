# provide URI to constructor, or use environment variable
from readline import redisplay  # the display() function is most likely only available to jupyter notebook
from markdown import Markdown   # TODO: There;s an issue with the import that needs fixing
import pymongo
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
from dotenv import load_dotenv
import os


# this is based on the mongoDB vector database tutorial from the documentation ot get a better understanding of how vector datbases works
# load the environment variables
load_dotenv()


#TODO: instead of huggingface, try using OpenAI model isntead
# Perform the relevant configuration to the default llama-index settings

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


#ollama
#Settings.llm = Ollama(model="mistral", request_timeout=30.0)   

mongo_uri = os.getenv("MONGO_URI")
#openai_key = os.getenv("OPENAI_API_KEY")

#print("Mongo URI: ", mongo_uri)
#print(mongo_uri)  # print it out to see if the mongo_uri is set correctly --> test passed
#print("Open AI:", openai_key)  # print it out to see if the openai_key is set correctly --> test passed

# create the mongodb client instance 
# create a mongoDB client instance by passing the connection string
mongodb_client = pymongo.MongoClient(mongo_uri)

# embed_model = OpenAIEmbedding(embed_batch_size=10)  # note that since we changed the embedding model that we are working with, we will also need to adjust the index dimensionality
#Settings.embed_model = embed_model

# check if connection is successful or not
if mongodb_client:
    print("Successfull Connection to MongoDB Atlas")
else:
    print("Connection to MongoDB Atlas Failed")

# intialize a vector search object for the MongoDB atlas with the MongoDB client
store = MongoDBAtlasVectorSearch(mongodb_client, db_name="test-database", collection_name="uber_docs", index_name="default")
storage_context = StorageContext.from_defaults(vector_store=store)
uber_docs = SimpleDirectoryReader("/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/10k/").load_data()

# check the raw data that was loaded
#print("Loaded Uber Docs:")
#print(uber_docs)  --> uncomment this if you want to see the raw data that was loaded

index = VectorStoreIndex.from_documents(
    uber_docs, storage_context=storage_context
)

# print a confirmation message to indicate that the data has been indexed
print("Indexed Data")

#about the number of documents indexed or other metadata
print(index)

# Initial Size
print("Initial Vector Store Size:")
print(store._collection.count_documents({}))  # output: 2070
# get a ref_doc_id

response = index.as_query_engine().query("What was Uber's revenue?")
print("successful connection")
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
