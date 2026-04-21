from services.search import SearchService

def main():
    search_service = SearchService()

    while True:
        query = input("\nPergunta: ")

        if query.lower() == "sair":
            break

        results = search_service.search(query, k=1)

        print("\nResultados:\n")

        for r in results:
            print(f"[{r['title']} - {r['section']}]")
            print(r["text"])
            print("-" * 50)
            print("source:", r['source'])

if __name__ == "__main__":
    main()