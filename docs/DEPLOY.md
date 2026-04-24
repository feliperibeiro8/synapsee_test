# Plano de Deploy (AWS)

# Visão Geral

Este projeto consiste em um chatbot baseado em **Retrieval-Augmented Generation (RAG)**, que recebe perguntas em linguagem natural, recupera trechos relevantes de uma base de conhecimento e gera respostas utilizando um modelo de linguagem (LLM).

O sistema é composto por:

* Interface (Streamlit)
* Backend em Python (busca e geração)
* Índice vetorial (FAISS)
* API externa de LLM (Groq)

---

## Arquitetura Proposta na AWS

### 1. Interface (Frontend)

* **Serviço**: Amazon EC2 ou AWS Elastic Beanstalk
* A aplicação Streamlit será hospedada em uma instância EC2 leve
* Responsável por receber perguntas e exibir respostas

---

### 2. Lógica da aplicação (Backend)

* Executado na mesma instância EC2 (para simplificação)
* Responsável por:

  * Carregar o índice FAISS
  * Realizar busca semântica
  * Construir o prompt
  * Chamar a API do LLM (Groq)

---

### 3. Armazenamento de Dados

* **Amazon S3**

  * Armazena documentos originais e processados (`chunks.json`)
* **FAISS index**

  * Pode ser armazenado localmente na EC2 ou carregado do S3 na inicialização

---

### 4. Integração com LLM

* Uso de API externa (Groq)
* O backend envia o prompt e recebe a resposta gerada

---

## Fluxo de Dados

1. O usuário envia uma pergunta pela interface
2. A aplicação gera o embedding da pergunta
3. O FAISS busca os chunks mais relevantes
4. O sistema monta um prompt com o contexto recuperado
5. O prompt é enviado para a API do LLM (Groq)
6. A resposta gerada é retornada para o frontend
7. As fontes utilizadas são exibidas junto da resposta

---

## Estratégia de Escalabilidade

### Escala Vertical

* Aumentar recursos da instância EC2 (CPU/RAM)

### Escala Horizontal

* Múltiplas instâncias EC2 atrás de um **Application Load Balancer (ALB)**
* Aplicação é stateless, permitindo replicação

### Cache

* Uso de **Amazon ElastiCache (Redis)** para:

  * Perguntas frequentes
  * Respostas já geradas

### Processamento Assíncrono (futuro)

* Uso de **SQS + AWS Lambda** para tarefas mais pesadas

---

## Riscos e Desafios

### 1. Latência da API

* Chamadas ao LLM podem ser lentas
* Mitigação: reduzir tamanho do prompt e usar cache

---

### 2. Limites da API (Groq)

* Pode haver restrição de uso no plano gratuito
* Mitigação: controle de requisições e fallback

---

### 3. Custos

* Uso de EC2 e APIs pode gerar custos
* Mitigação: monitoramento e auto scaling

---

### 4. Tempo de Inicialização

* Carregamento do FAISS pode ser lento
* Mitigação: manter instância aquecida

---

### 5. Atualização dos Dados

* Mudanças na base exigem reprocessamento
* Mitigação: pipeline de reindexação periódica

---

## Segurança

* Armazenar chaves de API no **AWS Secrets Manager**
* Controle de acesso com IAM
* Uso de HTTPS via **AWS Certificate Manager + ALB**

---

## Melhorias Futuras

* Substituir Streamlit por frontend em React + API REST
* Utilizar banco vetorial gerenciado (ex: OpenSearch, Pinecone)
* Containerizar com Docker e usar ECS/EKS
* Adicionar autenticação de usuários (Amazon Cognito)

---

## Conclusão

A arquitetura proposta permite colocar o chatbot em produção de forma escalável e eficiente, utilizando serviços da AWS. Além disso, possibilita evolução futura para maior performance, segurança e experiência do usuário.
