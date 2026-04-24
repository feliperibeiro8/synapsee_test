from services.search import SearchService
from services.chatbot import build_prompt, generate_answer

def main():
    search_service = SearchService()

    while True:
        query = input("\nPergunta: ")

        if query.lower() == "sair":
            break

        chunks = search_service.search(query, k=5)

        if not chunks:
            print("\nResposta:\nNão encontrei informação relevante.")
            continue

        prompt = build_prompt(query, chunks)
        
        print("\nPROMPT PARA DEBUG:\n")
        print(prompt)

        answer = generate_answer(prompt)

        print("\nResposta:\n")
        print(answer)


if __name__ == "__main__":
    main()