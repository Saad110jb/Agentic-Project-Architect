import os
from pinecone import Pinecone
from crewai.tools import tool
from sentence_transformers import SentenceTransformer # Free local embeddings

# Load the free model (runs locally on your PC)
model = SentenceTransformer('all-MiniLM-L6-v2')

@tool("trend_researcher")
def query_tech_trends(user_query: str):
    """
    Queries the vector database for industry trends.
    """
    try:
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))

        # 1. Generate embedding locally (FREE)
        query_vector = model.encode(user_query).tolist()

        # 2. Search Pinecone
        results = index.query(vector=query_vector, top_k=3, include_metadata=True)
        
        if not results['matches']:
            return "No specific trends found in database."

        context = ""
        for match in results['matches']:
            context += f"Trend: {match['metadata'].get('title')}\nSummary: {match['metadata'].get('summary')}\n\n"
        return context
    except Exception as e:
        return f"Error executing tool: {str(e)}"