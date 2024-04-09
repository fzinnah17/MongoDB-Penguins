
import os

from dotenv import load_dotenv
#from openai import OpenAI
import pymongo
from llama_index.core.settings import Settings
from llama_index.core import VectorStoreIndex
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core import VectorStoreIndex, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.replicate import Replicate
from llama_index.core.postprocessor import LLMRerank
from transformers import AutoTokenizer, AutoModelForCausalLM
from fpdf import FPDF
import base64
import certifi

from cover_letter_prompt import COVER_LETTER_PROMPT_TEMPLATE

load_dotenv()

def hardcode_env_vars():
    #os.environ["ANTHROPIC_API_KEY"] = "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"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    #os.environ["MONGO_URI"] = "mongodb+srv://adas006:ayan@embeddingsdata.7urn3ch.mongodb.net/?retryWrites=true&w=majority&appName=EmbeddingsData"

def initialize_global_settings():
    # os.environ["ANTHROPIC_API_KEY"] = "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"
    #model = AutoModelForCausalLM.from_pretrained("davidkim205/Rhea-72b-v0.5")  # a huggingface model
    model = OpenAI(model="gpt-4", max_tokens=3000, api_version=os.environ["OPENAI_API_KEY"])
    Settings.llm = model
    '''
    Replicate(
        model="meta/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
        is_chat_model=True,
        additional_kwargs={"max_new_tokens": 1024}
)  '''
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

def main(
        job_description_str: str = "Software Engineer at Google"
    ):

    # Hardcode environment variables
    hardcode_env_vars()

    # Initialize global settings
    initialize_global_settings()

    # Connect to database
    mongodb_client = pymongo.MongoClient(
        os.environ["MONGO_URI"], tlsCAFile=certifi.where()
    )
    mongo_vector_store = MongoDBAtlasVectorSearch(
        mongodb_client,
        db_name="test-database",
        collection_name="ayan_docs",
        index_name="default"
    )
    mongo_index = VectorStoreIndex.from_vector_store(
        vector_store=mongo_vector_store,
    )

    # Assemble query engine
    query_engine = RetrieverQueryEngine(
        retriever=VectorIndexRetriever(
            index=mongo_index,
            similarity_top_k=50,
        ),
        response_synthesizer=get_response_synthesizer()
    )

    # Applicant information
    applicant_information_str = query_engine.query(
        "Provide applicant personal information, like name, address, and contact information.",
    )

    # Application skills
    applicant_skills_str = query_engine.query(
        "Provide applicant skills, like programming languages, frameworks, and tools."
    )

    # Applicant experiences
    applicant_experiences_str = query_engine.query(
        "Provide applicant experiences, like previous jobs, projects, and education."
    )

    # Generate cover letter
    cover_letter = Settings.llm.complete(
        COVER_LETTER_PROMPT_TEMPLATE.format(
            applicant_personal_information=applicant_information_str,
            applicant_skills=applicant_skills_str,
            applicant_experiences=applicant_experiences_str,
            job_description=job_description_str
        )
    )

    
    return cover_letter

if __name__ == "__main__":
    print(main())