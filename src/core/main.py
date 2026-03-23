from query_handler import handle_query

def main():
    print("🎨 Welcome to CreativeLab!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        response = handle_query(user_input)
        print(f"CreativeLab: {response}\n")

if __name__ == "__main__":
    main()
