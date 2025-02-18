import os
import base64
from IPython.display import Image, display
from langchain_text_splitters import CharacterTextSplitter
from unstructured.documents.elements import Text, Table, CompositeElement
from unstructured.partition.pdf import partition_pdf
from dotenv import load_dotenv
load_dotenv()

# Load environment variables from .env file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

path = "trial/"
fname = "7-Agentic-RAG-System.pdf"

# === PDF PROCESSING FUNCTIONS === #
def extract_pdf_elements(path, fname): # later change to filepath only
    """
    Extract text, tables, and images from a PDF.
    path: File path, which is used to dump images (.jpg)
    fname: File name
    
    Returns:
    text_data: List[str] - Text chunks from PDF
    table_data: List[str] - HTML table representations
    image_data: List[str] - Base64 encoded images
    """

    # Partition PDF into chunks and extract images, tables, and text
    chunks = partition_pdf(filename=path+fname,
                           infer_table_structure=True,                   # Extract tables
                           strategy="hi_res",                            # Mandatory for table extraction
                           extract_image_block_types=["Image", "Table"], # Extract images and table images
                           extract_image_block_to_payload=True,          # True, extract base64 images for API
                           chunking_strategy="by_title",                 # Can also use 'basic'
                           max_characters=4000,                          # Defaults to 500
                           new_after_n_chars=3800, 
                           combine_text_under_n_chars=2000,              # Defaults to 0
                           )   

    text_data, table_data, image_data = [], [], [] 
    
    # Extract Text
    text_data = [chunk.text for chunk in chunks if isinstance(chunk, Text)] 
    
    # Extract Tables (Including Nested in CompositeElement)
    for chunk in chunks:
        if isinstance(chunk, Table):
            table_data.append(chunk.metadata.text_as_html) # Extract table as HTML
        elif isinstance(chunk, CompositeElement):
            chunk_elements = chunk.metadata.orig_elements
            for el in chunk_elements:
                if "Table" in str(type(el)):
                    table_data.append(el.metadata.text_as_html)
             
    # Extract Images (Base64)
    for chunk in chunks:
        if "CompositeElement" in str(type(chunk)):
            chunk_els = chunk.metadata.orig_elements
            for el in chunk_els:
                if "Image" in str(type(el)):
                    image_data.append(el.metadata.image_base64)
                    
    return text_data, table_data, image_data