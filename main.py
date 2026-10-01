from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from pdf_processor import save_uploaded_pdfs, extract_text_and_chunk
from vector_store import initialize_vector_database
from rag_service import generate_rag_response
from pydantic import BaseModel

app = FastAPI(title="AI Study Assistant RAG")

# Serve static frontend folder
app.mount("/static", StaticFiles(directory="static"), name="static")

class QuestionRequest(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
async def read_index():
    """Serves the single-file HTML user interface."""
    html_path = os.path.join("static", "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    return "UI file not found. Please place index.html in the static folder."

@app.post("/api/upload")
async def upload_pdfs(files: list[UploadFile] = File(...)):
    """API endpoint to upload 1 to 10 PDFs, extract text, chunk, and embed them."""
    if not (1 <= len(files) <= 10):
        raise HTTPException(status_code=400, detail="Please upload between 1 and 10 PDF files at a time.")
    
    try:
        saved_paths = save_uploaded_pdfs(files)
        chunks, metadatas = extract_text_and_chunk(saved_paths)
        total_chunks = initialize_vector_database(chunks, metadatas)
        return {
            "status": "success", 
            "message": f"Successfully processed {len(files)} PDFs into {total_chunks} local vector embeddings!"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/api/ask")
async def ask_question(payload: QuestionRequest):
    """API endpoint to handle student study queries via RAG."""
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    result = generate_rag_response(payload.question)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)