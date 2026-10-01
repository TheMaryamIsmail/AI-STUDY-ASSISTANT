import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directories
PDF_DIR = os.path.join(BASE_DIR, "data", "pdfs")
CHROMA_DIR = os.path.join(BASE_DIR, "data", "chroma_db")

# Ensure directories exist
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)

# API Configuration (Pulling directly from your .env file)
GROQ_API_KEY = os.getenv("THE_API", "")
# config.py
GROQ_MODEL = "openai/gpt-oss-120b"