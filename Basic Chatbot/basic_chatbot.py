def chatbot_response(user_input):
    """Function to provide predefined responses based on user input"""
    # Convert the user input to lowercase to handle different cases
    user_input = user_input.lower()

    # Provide predefined responses based on user input using conditional statements
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you!"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot, and I don't have a name yet!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase?"

# Main loop to interact with the user
print("Welcome to the chatbot! Type 'bye' to exit.")
while True:
    # Get input from the user
    user_input = input("User: ")

    # If the user types 'bye', exit the chat
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Get the chatbot's response
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
