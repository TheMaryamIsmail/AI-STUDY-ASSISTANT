import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_DIR

# Use a lightweight, high-performance local embedding model
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def get_chroma_client():
    return chromadb.PersistentClient(path=CHROMA_DIR)

def initialize_vector_database(chunks, metadatas):
    """Embeds text chunks and saves them locally into ChromaDB."""
    client = get_chroma_client()
    collection_name = "python_study_assistant"
    
    # Recreate collection to ensure a fresh setup
    try:
        client.delete_collection(name=collection_name)
    except Exception:
        pass

    collection = client.create_collection(
        name=collection_name, 
        embedding_function=embedding_fn
    )

    ids = [str(i) for i in range(len(chunks))]
    
    # Add chunks to collection in batches
    collection.add(
        documents=chunks,
        metadatas=metadatas,
        ids=ids
    )
    return len(chunks)

def query_vector_database(query_text, n_results=3):
    """Retrieves the most relevant chunks from ChromaDB."""
    client = get_chroma_client()
    collection = client.get_collection(
        name="python_study_assistant", 
        embedding_function=embedding_fn
    )
    
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    return results['documents'][0], results['metadatas'][0]