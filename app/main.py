from pipeline.data_loader import load_markdowns
from pipeline.preprocessing import process_documents
from pipeline.chunking import chunk_text

def main():
    docs = load_markdowns()
    docs_clean = process_documents(docs)
    
    all_chunks = []

    for doc in docs_clean:
        chunks = chunk_text(doc['text'])

        for chunk in chunks:
            all_chunks.append({
                "text": chunk,
                "title": doc["title"],
                "source": doc["source"],
                "section": doc["section"]
            })
    
    print(f"{len(docs)} documentos carregados")
    print(f"{len(all_chunks)} chunks gerados")
    print("")

    for i, chunk in enumerate(all_chunks):
        print(f"\n--- Chunk {i} ({chunk['title']}, {chunk['section']}, {chunk['source']}) ---")
        print(chunk["text"])

if __name__ == "__main__":
    main()

