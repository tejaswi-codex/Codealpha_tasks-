# Function for chatbot replies
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hi" in user_input or "hello" in user_input or "hey" in user_input:
        return "Hi! How are you?"

    # Asking chatbot condition
    elif "how are you" in user_input:
        return "I'm good, thanks!"

    # User feeling
    elif "good" in user_input or "fine" in user_input:
        return "That's nice to hear"

    # Asking chatbot name
    elif "what is your name" in user_input:
        return "I'm a simple Python chatbot"

    # Asking chatbot abilities
    elif "what can you do" in user_input:
        return "I can answer simple questions. How can I help you?"

    # Weather / temperature
    elif "temperature" in user_input or "weather" in user_input:
        return "Today's temperature is pleasant and sunny"

    # Nice response
    elif "nice" in user_input:
        return "I'm glad you liked it "

    # Okay message
    elif "okay" in user_input or "ok" in user_input:
        return "Alright"

    # Thank you message
    elif "thank" in user_input or "thanks" in user_input:
        return "You're welcome "

    # Exit message
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day"

    # Default response
    else:
        return "Sorry, I didn't understand that."


# Main chatbot loop
print("Chatbot started! Type 'bye' to exit.")

while True:
    user = input("You: ")

    response = chatbot_response(user)
    print("Bot:", response)

    # Break condition
    if "bye" in user.lower() or "goodbye" in user.lower():
        break

# Ending message
print("Chatbot session ended successfully.")
