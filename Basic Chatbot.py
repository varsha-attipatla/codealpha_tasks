def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("🤖 Chatbot: Hi there!")
        elif user_input in ["how are you", "how are you doing"]:
            print("🤖 Chatbot: I'm fine, thanks! How can I help you?")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

# Start the chatbot
chatbot()
