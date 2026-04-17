import json, os

def save_chunks(chunks, path):
    print(f"Caminho: {path}")  # debug
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print("Arquivo salvo!")