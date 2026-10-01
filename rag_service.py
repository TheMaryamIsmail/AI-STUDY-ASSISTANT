import requests
from config import GROQ_API_KEY, GROQ_MODEL
from vector_store import query_vector_database

def generate_rag_response(question: str):
    """Performs RAG workflow: Retrieves chunks, builds prompt, and queries LLM."""
    try:
        # 1. Retrieve relevant contexts
        retrieved_docs, metadatas = query_vector_database(question, n_results=3)
        context_text = "\n\n---\n\n".join(retrieved_docs)
    except Exception as e:
        return {
            "answer": f"Vector Database Error: Please make sure you have uploaded and processed your PDF files in Step 1 first! Details: {str(e)}",
            "sources": []
        }
    
    # 2. Construct Prompt
    system_prompt = (
        "You are an expert AI Study Assistant specializing in Python programming. "
        "Answer the user's question accurately using ONLY the provided context extracted from course PDFs. "
        "If the answer is not available in the context, state clearly that you cannot find the answer in the provided chapters."
    )
    
    user_prompt = f"Context:\n{context_text}\n\nQuestion: {question}"

    # 3. Call Groq API Endpoint
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 512
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            json=payload,
            headers=headers,
            timeout=30
        )
        res_json = response.json()
        
        if "choices" in res_json:
            answer = res_json['choices'][0]['message']['content']
        else:
            answer = f"API Error Response: {res_json}"
            
    except Exception as e:
        answer = f"Error connecting to LLM API: {str(e)}"

    return {
        "answer": answer,
        "sources": list(set([m['source'] for m in metadatas]))
    }