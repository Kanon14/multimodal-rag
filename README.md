# 📚 Multimodal RAG System
An advanced **Multimodal Retrieval-Augmented Generation (RAG) System** built with **LangChain**, **OpenAI GPT-4o**, and **ChromaDB**. This app allows users to upload research papers in PDF format, extract text, tables, and images, summarize them, and answer user queries using relevant information from the document.

## Features
- 📄 **PDF Extraction:** Extracts text, tables, and images from uploaded research papers using the Unstructured library.
- 🧠 **Summarization:** Generates concise summaries for text, tables, and images using GPT-4o.
- 💾 **ChromaDB Storage:** Stores summarized data in a vector database for efficient retrieval.
- 🔍 **Multimodal Retrieval:** Retrieves relevant text, tables, and images to answer user queries.
- 🎨 **Interactive Streamlit UI:** User-friendly interface for uploading PDFs and asking questions.
- 📈 **Persistent Storage:** Keeps embeddings stored locally across sessions.

## Project Setup
### Prerequisites
- Python 3.8+
- Streamlit – Interactive web app framework
- LangChain – Framework for building RAG systems
- OpenAI GPT-4o – Summarization and query answering
- ChromaDB – Vector database for efficient retrieval
- Unstructured – For extracting structured content from PDFs
- dotenv – Manage environment variables securely
- All the required libraries or packages can be found in `requirements.txt`.

*Note:*  As for **Unstructured**, required the following system dependencies if they are not available on your system. Refer to the GitHub repo of [unstructured](https://github.com/Unstructured-IO/unstructured).
* libmagic-dev (filetype detection)
* [poppler-utils](https://pdf2image.readthedocs.io/en/latest/installation.html) (images and PDFs)
* [tesseract-ocr](https://tesseract-ocr.github.io/tessdoc/Installation.html) (images and PDFs, install tesseract-lang for additional language support)

### Installation
1. **Clone the repository:**
```bash
git clone https://github.com/Kanon14/multimodal-rag.git
cd multimodal-rag
```

2. **Create and activate a Conda environment:**
```bash
conda create -n multimodal-rag python=3.10 -y
conda activate multimodal-rag
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create a `.env` file in the root directory:**
```ini
OPENAI_API_KEY=your-openai-api-key
LANGCHAIN_API_KEY=your-langchain-api-key
LANGCHAIN_TRACING_V2=true
```

### How to Run
1. **Execute the project:**
```bash
streamlit run streamlit_app.py
```
2. **Then, access the application via your web browser:**
```bash
open http://localhost:<port>
```

## Acknowledgements
- Inspired by advancements in RAG (Retrieval-Augmented Generation).
- Built with tools from OpenAI, LangChain, ChromaDB, and Unstructured.
- Developed with love for the AI and research community.