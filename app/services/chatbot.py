import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
    )

def build_prompt(question, chunks):
    context = "\n\n".join([chunk["text"] for chunk in chunks ])

    prompt = f"""
You are a neuroscience expert.

Answer the question using ONLY the context below.
- Be clear and concise (3-4 sentences).
- If the answer is not in the context, say "Infortunely I don't know about this topic".

Example:
Question: What is the hippocampus?
Answer: The hippocampus is a brain structure involved in memory formation and spatial navigation.

Context:
{context}

Question:
{question}

Answer:
"""
    return prompt

def generate_answer(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
    