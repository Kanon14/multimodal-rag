import streamlit as st
from utils import (
    extract_pdf_elements, generate_text_summaries, generate_image_summary,
    create_multivector_retriever
)
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# Initialize Streamlit app
st.set_page_config(page_title="Multimodal RAG", layout="wide")
st.title("📄 Multimodal RAG System")

# Sidebar for PDF Upload
st.sidebar.header("Upload PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

# Query Input
query = st.text_input("🔍 Ask a Question:", placeholder="Type your query here...")

# Process PDF and Generate Summaries
if uploaded_file is not None:
    st.sidebar.success("✅ PDF Uploaded Successfully!")
    st.sidebar.write("Extracting content...")

    # Step 1: Extract elements from the uploaded PDF
    text_data, table_data, image_data = extract_pdf_elements(uploaded_file)

    # Step 2: Generate Summaries
    text_summaries, table_summaries = generate_text_summaries(text_data, table_data, summarize_texts=True)
    image_summaries = generate_image_summary(image_data)

    # Step 3: Store Summaries & Extracted Data in ChromaDB
    vectorstore = Chroma(collection_name="multimodal_rag", embedding_function=OpenAIEmbeddings())
    retriever = create_multivector_retriever(vectorstore, text_summaries, text_data, table_summaries, table_data, image_summaries, image_data)

    st.success("✅ PDF Processed Successfully! Data Stored in Vector & Document Store.")

# Submit Button (Next Step: Query Processing)
if st.button("Submit Query"):
    if uploaded_file is None:
        st.warning("⚠ Please upload a PDF before querying.")
    elif query.strip() == "":
        st.warning("⚠ Please enter a query.")
    else:
        st.info("✅ Processing query... (Next step: Retrieval & Answering)")
