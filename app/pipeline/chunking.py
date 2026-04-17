def chunk_text(text, chunk_size=120, overlap=30, min_words=50):
    words = text.split()
    chunks = []
    start = 0
    n = len(words)

    while start < n:
        end = start + chunk_size
        chunk_words = words[start:end]

        # Evita chunks muito pequenos
        if len(chunk_words) < min_words:
            break

        chunk = " ".join(chunk_words)
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks