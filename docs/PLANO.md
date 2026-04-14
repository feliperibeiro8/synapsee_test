# PLANO.md — Desafio AI Engineer (Synapsee)

## 1. Arquitetura

A solução seguirá o padrão **RAG (Retrieval-Augmented Generation)**:

* **Ingestão:** leitura de arquivos Markdown + extração de seções
* **Chunking:** divisão por seções com ~300–500 tokens e overlap
* **Embeddings:** modelo local (`all-MiniLM-L6-v2`)
* **Banco vetorial:** FAISS (local)
* **Retrieval:** busca por similaridade (top-k = 3–5)
* **Geração:** LLM via API gratuita (Groq - LLaMA 3)
* **Interface:** Streamlit

---

## 2. Fluxo

1. Usuário faz uma pergunta
2. Pergunta → embedding
3. Busca retorna chunks relevantes
4. Prompt é montado com contexto
5. LLM gera resposta
6. Interface exibe resposta + fontes

---

## 3. Engenharia de Prompt

* **Persona + restrição:** especialista, uso apenas do contexto
* **Few-shot:** exemplos para padronizar respostas
* **Chain-of-thought:** respostas estruturadas

---

## 4. Etapas e estimativa de tempo

1. Setup do projeto e leitura dos dados — **3h**
2. Implementação do parser de Markdown — **3h**
3. Estratégia de chunking — **2h**
4. Geração de embeddings (local) — **3h**
5. Indexação no FAISS — **3h**
6. Implementação do retrieval — **2h**
7. Construção e ajuste de prompts — **3h**
8. Integração com LLM (Groq) — **3h**
9. Interface com Streamlit — **4h**
10. Testes e ajustes finais — **4h**

**Tempo total estimado: 30 horas ~10 dias**

---

## 5. Avaliação do chatbot

* **Relevância:** resposta condiz com o contexto recuperado
* **Fidelidade:** evita informações fora do contexto
* **Clareza:** resposta bem estruturada
* **Fontes:** indica corretamente os trechos utilizados

Teste com perguntas:

* conceituais
* comparativas
* aplicadas ao contexto
