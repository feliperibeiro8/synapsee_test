from pathlib import Path

data_path = Path("app/data/raw")

def load_markdowns():
    docs = []

    for file in data_path.glob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            docs.append({
                "title": file.name,
                "content":f.read()
            })
    
    return docs