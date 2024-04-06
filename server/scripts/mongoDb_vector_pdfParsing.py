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
from ReadLinks import node0, node1, node2, node3, node4, node5, node6, node7, node8, googleNode, apple_Node, microsoftNode, trunkToolsNode, mongodb_Node, nomic_Node, etsy_Node, americanExpress_Node, chase_Node  # import the html nodes so we can read them
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
store = MongoDBAtlasVectorSearch(mongodb_client, db_name="test-database", collection_name="ayan_docs", index_name="default")
storage_context = StorageContext.from_defaults(vector_store=store)
ayan_docs = SimpleDirectoryReader("/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/Ayan/").load_data()


# check the raw data that was loaded
#print("Loaded Uber Docs:")
#print(uber_docs)  --> uncomment this if you want to see the raw data that was loaded

index = VectorStoreIndex.from_documents(
    ayan_docs, storage_context=storage_context
)

#define the index_struct
index_struct = { 
    "text" : "<Node Text Content>",
    "embedding " : ["<numerical array embeddings>"],
}

print("Individual Nodes:")
nodes = [node0, node1, node2, node3, node4, node5, node6, node7, node8, googleNode, apple_Node, microsoftNode, trunkToolsNode, mongodb_Node, nomic_Node, etsy_Node, americanExpress_Node, chase_Node]


for i, node in enumerate(nodes):
    print(f"Node {i} is of type {type(node)}")

mongo_index = VectorStoreIndex.from_vector_store(
    vector_store=store
)

# last attempt at insering nodes
db = mongodb_client['test-database']
collection = db['ayan_docs']

# Convert your nodes to dictionaries
#nodes_dict = [node.__dir__ for node in nodes]

# Convert your nodes to dictionaries
# Flatten your nodes if they are lists of dictionaries
#nodes_flat = [item for sublist in nodes for item in sublist if isinstance(sublist, list) and isinstance(item, dict)]

# Insert the nodes into the collection
#collection.insert_many(nodes_flat)
# Convert your nodes to dictionaries, skipping nodes without a __dict__ attribute

'''
nodes_dict = [vars(node) for node in nodes if hasattr(node, '__dict__')]

# insert all
collection.insert_many(nodes_dict)

'''

#mongo_index.add([node0, node1, node2, node3, node4, node5, node6, node7, node8, googleNode, apple_Node, microsoftNode, trunkToolsNode, mongodb_Node, nomic_Node, etsy_Node, americanExpress_Node, chase_Node])


# add the node directly to the index
index._add_nodes_to_index(nodes=node0,index_struct=index_struct)

index._add_nodes_to_index(nodes=node1, index_struct=index_struct)

index._add_nodes_to_index(nodes=node2, index_struct=index_struct)

index._add_nodes_to_index(nodes=node3, index_struct=index_struct)

index._add_nodes_to_index(nodes=node4, index_struct=index_struct)

index._add_nodes_to_index(nodes=node5, index_struct=index_struct)

index._add_nodes_to_index(nodes=node6, index_struct=index_struct)

index._add_nodes_to_index(nodes=node7, index_struct=index_struct)

index._add_nodes_to_index(nodes=node8, index_struct=index_struct)

index._add_nodes_to_index(nodes=googleNode, index_struct=index_struct)

index._add_nodes_to_index(nodes=apple_Node, index_struct=index_struct)

index._add_nodes_to_index(nodes=microsoftNode, index_struct=index_struct)

index._add_nodes_to_index(nodes=trunkToolsNode, index_struct=index_struct)

index._add_nodes_to_index(nodes=mongodb_Node, index_struct=index_struct)

index._add_nodes_to_index(nodes=nomic_Node, index_struct=index_struct, show_progress=True)

index._add_nodes_to_index(nodes=etsy_Node, index_struct=index_struct, show_progress=True)

index._add_nodes_to_index(nodes=americanExpress_Node, index_struct=index_struct)

index._add_nodes_to_index(nodes=americanExpress_Node, index_struct=index_struct)

index._add_nodes_to_index(nodes=chase_Node, index_struct=index_struct)
# print a confirmation message to indicate that the data has been indexed
print("Indexed Data")

#about the number of documents indexed or other metadata
print(index)

# Initial Size
print("Initial Vector Store Size:")
print(store._collection.count_documents({}))  # output: 2070
# get a ref_doc_id

query="What do you know about etsy from your vector index"
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
