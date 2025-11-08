from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import json
import os

def build_embeddings():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    with open("data/news_data.json", "r", encoding="utf-8") as f:
        news_data = json.load(f)

    texts = [n["content"] for n in news_data]
    embeddings = model.encode(texts)

    os.makedirs("embeddings", exist_ok=True)
    faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
    faiss_index.add(np.array(embeddings))
    faiss.write_index(faiss_index, "embeddings/index.faiss")

    print("✅ FAISS index built and saved.")


if __name__ == "__main__":
    articles = build_embeddings()
