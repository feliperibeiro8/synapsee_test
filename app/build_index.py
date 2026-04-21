import json, faiss
from sentence_transformers import SentenceTransformer

def load_chunks(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("Loading chunks...")
    chunks = load_chunks("app/data/processed/chunks.json")

    print("Loadinf model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    texts = [chunk["text"] for chunk in chunks]

    print("Generating embeddings...")
    embeddings = model.encode(texts,  show_progress_bar=True)

    print("Creating FAISS index...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    print("Saving index...")
    faiss.write_index(index, "app/data/processed/faiss.index")

    print("Index sucessfull created!")

if __name__ == "__main__":
    main()