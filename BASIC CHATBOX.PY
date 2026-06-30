# CodeAlpha_ProjectName basic chatbox
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you for asking! How are you?"
    elif "your name" in user_input:
        return "I am a simple rule-based Python chatbot created for CodeAlpha."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a wonderful day ahead!"
    elif "help" in user_input:
        return "I can respond to basic greetings like 'hello', 'how are you', or 'bye'."
    else:
        return "I'm sorry, I don't quite understand that. Could you try phrasing it differently?"

def start_chatbot():
    print("--- Basic Rule-Based Chatbot ---")
    print("Type 'bye' or 'goodbye' to exit the chat.")
    
    while True:
        user_input = input("\nYou: ")
        response = get_bot_response(user_input)
        print(f"Bot: {response}")
        
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

if __name__ == "__main__":
    start_chatbot()
