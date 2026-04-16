import re

def extract_source(text: str) -> str:
    match = re.search(r"\*\*Fonte:\*\*\s*(.+)", text, flags=re.IGNORECASE)
    return match.group(1).strip() if match else None

def remove_source(text: str):
    return re.sub(r"\*\*Fonte:\*\*.*", "", text, flags=re.IGNORECASE).strip()

def extract_title(text: str) -> str:
    first_line = text.split("\n")[0].strip()
    first_line = first_line.lstrip("#").strip()
    return first_line if first_line else None

def split_by_sections(text: str):
    sections = []

    current_section = None
    current_level = None
    current_text = []

    for line in text.split("\n"):
        line = line.strip()

        # Detecta headers de nível 2 até 6 (##, ###, ####...)
        match = re.match(r"^(#{2,6})\s+(.*)", line)

        if match:
            # salva seção anterior
            if current_text:
                sections.append({
                    "section": current_section if current_section else "Sem seção",
                    "level": current_level,
                    "text": "\n".join(current_text).strip()
                })
                current_text = []

            current_level = len(match.group(1))
            current_section = match.group(2).strip()

        else:
            current_text.append(line)

    # última seção
    if current_text:
        sections.append({
            "section": current_section if current_section else "Sem seção",
            "level": current_level,
            "text": "\n".join(current_text).strip()
        })

    return sections

def clean_text(text: str) -> str:
    """
    Limpeza leve para preservar estrutura útil para embeddings
    """

    # Remove markdown básico
    text = re.sub(r"#", "", text)
    text = re.sub(r"\*\*", "", text)

    # Remove referências tipo [1], [23]
    text = re.sub(r"\[\d+\]", "", text)

    # Normaliza quebras de linha (mantém parágrafos)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

def process_documents(docs):
    processed = []

    skip_sections = {
        "references",
        "see also",
        "external links",
        "notes"
    }

    for doc in docs:
        text = doc["content"]

        source = extract_source(text)
        text = remove_source(text)

        title = extract_title(text)
        sections = split_by_sections(text)

        for sec in sections:
            section_name = sec["section"].lower() if sec["section"] else ""

            # ignora seções irrelevantes
            if section_name in skip_sections:
                continue

            cleaned = clean_text(sec["text"])

            # mantém contexto rico para o próximo passo (chunking)
            enriched_text = f"{title}\n{sec['section']}\n{cleaned}"

            processed.append({
                "text": enriched_text,
                "title": title,
                "section": sec["section"],
                "level": sec["level"],
                "source": source
            })

    return processed