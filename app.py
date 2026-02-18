from core.orchestrator import BFSIAssistant


def main():

    assistant = BFSIAssistant()

    print("BFSI Call Center AI Assistant Ready\n")

    while True:
        query = input("User: ").strip()
        if not query:
            print("Assistant: Please enter a valid query.\n")
            continue


        if query.lower() == "exit":
            break

        response = assistant.handle_query(query)

        print("\nAssistant:", response, "\n")


if __name__ == "__main__":
    main()
