import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model and FAISS index
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("embeddings/index.faiss")

# Load news data
with open("data/news_data.json", "r", encoding="utf-8") as f:
    news_data = json.load(f)

# Function to retrieve most relevant news articles
def retrieve_news(query, k=3):
    query_emb = model.encode([query])
    distances, indices = index.search(np.array(query_emb), k)
    return [news_data[i]["content"] for i in indices[0]]

# ✅ Entry point
if __name__ == "__main__":
    print("🔎 Welcome to the News Retriever!")
    while True:
        query = input("\nEnter your news query (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("👋 Exiting...")
            break

        results = retrieve_news(query)
        print("\nTop related news:")
        for idx, res in enumerate(results, 1):
            print(f"{idx}. {res}\n")
