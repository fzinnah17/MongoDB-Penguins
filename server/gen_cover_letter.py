
import os

import pymongo
from llama_index.core.settings import Settings
from llama_index.core import VectorStoreIndex
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core import VectorStoreIndex, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import LLMRerank
from fpdf import FPDF
import base64

from cover_letter_prompt import COVER_LETTER_PROMPT_TEMPLATE

def hardcode_env_vars():
    os.environ["ANTHROPIC_API_KEY"] = "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"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["MONGO_URI"] = "mongodb+srv://adas006:ayan@embeddingsdata.7urn3ch.mongodb.net/?retryWrites=true&w=majority&appName=EmbeddingsData"

def initialize_global_settings():
    os.environ["ANTHROPIC_API_KEY"] = "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"
    Settings.llm = Anthropic(
        model="claude-3-haiku-20240307"
        # model="claude-3-opus-20240229"
    )
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
        os.getenv("MONGO_URI")
    )
    mongo_vector_store = MongoDBAtlasVectorSearch(
        mongodb_client,
        db_name="test-database",
        collection_name="uber_docs",
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

    
    pdf = FPDF()
 
    # Add a page
    pdf.add_page()
    
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    
    # create a cell
    pdf.cell(200, 10, txt = "GeeksforGeeks", 
            ln = 1, align = 'C')
    
    # add another cell
    pdf.cell(200, 10, txt = cover_letter,
            ln = 2, align = 'C')
    
    # save the pdf with name .pdf
    # pdf.output("GFG.pdf") 
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    return html

if __name__ == "__main__":
    print(main())
