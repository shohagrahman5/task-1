def get_reply(message):
    """Return a response based on the user's message."""
    message = message.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi! Nice to meet you."
    elif message in ("how are you", "how are you?"):
        return "I'm fine, thanks! How can I help you?"
    elif message in ("what is your name", "what is your name?"):
        return "I'm CodeAlpha Bot, a simple Python chatbot."
    elif message in ("help", "what can you do"):
        return "I can respond to greetings, simple questions, and goodbye."
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't understand that yet. Try saying hello or help."


def main():
    print("===== CODEALPHA BASIC CHATBOT =====")
    print("Chat with me! Type 'bye' to end the conversation.")

    while True:
        user_message = input("\nYou: ")
        reply = get_reply(user_message)
        print("Bot:", reply)

        if user_message.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()
