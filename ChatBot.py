import random

# Define rules and responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm good, thank you! How about you?",
    "good morning": "Good morning! How can I assist you?",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
}

# Function to generate response based on input
def get_response(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return responses[key]
    return responses["default"]

# Main loop to run the chatbot
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
