from pipeline.data_loader import load_markdowns
from pipeline.preprocessing import process_documents
from pipeline.chunking import chunk_text
from utils import save_chunks

def main():
    docs = load_markdowns()
    docs_clean = process_documents(docs)

    all_chunks = []

    for doc in docs_clean:
        chunks = chunk_text(doc['text'])

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "id": f"{doc['section']}_{i}",
                "text": chunk,
                "title": doc["title"],
                "source": doc["source"],
                "section": doc["section"]
            })

    print(f"{len(docs)} documentos carregados")
    print(f"{len(all_chunks)} chunks gerados")

    save_chunks(all_chunks, "app/data/processed/chunks.json")

    print("Chunks salvos com sucesso!")

if __name__ == "__main__":
    main()

