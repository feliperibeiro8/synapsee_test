import json, faiss
from sentence_transformers import SentenceTransformer

class SearchService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.read_index("app/data/processed/faiss.index")

        with open("app/data/processed/chunks.json", "r", encoding="utf-8") as f:
            self.chunks = json.load(f)
    
    def capitalize_first(self, text):
        if not text:
            return text
        return text[0].upper() + text[1:]


    def search(self, query, k=5, score_threshold=1.2):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k)

        results = []

        for i, dist in zip(indices[0], distances[0]):
            chunk = self.chunks[i].copy()
            text = chunk["text"].lower()

            # Clean citation content
            if any(x in text for x in ["doi", "http", "isbn", "scholarpedia", "further reading"]):
                continue

            # Filter by score
            if dist > score_threshold:
                continue

            # Format for exhibition 
            chunk["text"] = self.capitalize_first(chunk["text"])
            chunk["score"] = float(dist)

            results.append(chunk)

        return results