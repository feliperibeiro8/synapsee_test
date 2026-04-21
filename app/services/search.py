import json, faiss
from sentence_transformers import SentenceTransformer

class SearchService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.read_index("app/data/processed/faiss.index")

        with open("app/data/processed/chunks.json", "r", encoding="utf-8") as f:
            self.chunks = json.load(f)
    
    def search(self, query, k=3):
        query_embedding = self.model.encode([query])

        distances, indices = self.index.search(query_embedding, k)

        results = []
        for i in indices[0]:
            results.append(self.chunks[i])
        
        results[0][0] = results[0][0].upper()
        return results