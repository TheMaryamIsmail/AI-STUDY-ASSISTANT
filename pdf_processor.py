import os
from pypdf import PdfReader
from config import PDF_DIR

def save_uploaded_pdfs(files):
    """Saves uploaded PDF files to the designated local directory."""
    saved_paths = []
    for file in files:
        file_path = os.path.join(PDF_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        saved_paths.append(file_path)
    return saved_paths

def extract_text_and_chunk(pdf_paths=None, chunk_size=500, overlap=50):
    """Extracts text from all PDFs and splits them into manageable chunks."""
    if not pdf_paths:
        pdf_paths = [os.path.join(PDF_DIR, f) for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    
    all_chunks = []
    metadata_list = []

    for path in pdf_paths:
        reader = PdfReader(path)
        filename = os.path.basename(path)
        
        full_text = ""
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                full_text += text + "\n"

        # Simple sliding chunk mechanism
        for i in range(0, len(full_text), chunk_size - overlap):
            chunk = full_text[i:i + chunk_size]
            if len(chunk.strip()) > 50:  # Avoid empty chunks
                all_chunks.append(chunk)
                metadata_list.append({"source": filename})

    return all_chunks, metadata_list