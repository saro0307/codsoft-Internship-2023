import random

# Define predefined rules and responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm just a chatbot.", "I don't have feelings, but I'm here to help."],
    "what's your name": ["you can call be JOI."],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure I understand.", "Can you please rephrase that?", "I don't have an answer for that."],
}

# Function to generate a response based on user input
def get_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive matching

    # Check if the user input matches any predefined rules
    for rule, response_list in responses.items():
        if rule in user_input:
            return random.choice(response_list)

    # If no specific rule matches, use the default response
    return random.choice(responses["default"])

# Main chat loop
print("Chatbot: Hi! How can I help you today? (Type 'bye' to exit)")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
