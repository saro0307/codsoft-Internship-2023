# codsoft-Internship-2023

# JOI Chatbot

## Overview

JOI Chatbot is a simple Python program that simulates a basic chatbot. The chatbot responds to user input based on predefined rules and provides appropriate responses. The program uses a set of rules and responses to handle common user queries and interactions.

## Features

- Responds to common greetings, inquiries, and farewells.
- Provides a default response for input it doesn't recognize.
- Case-insensitive matching for user input.
- Allows users to exit the chat by typing 'bye'.

## Usage

1. Ensure you have Python installed on your system.
2. Copy and paste the provided code into a Python file (e.g., `joi_chatbot.py`).
3. Run the program in a terminal or command prompt.
4. Enter your messages in the chat, and the chatbot will respond accordingly.
5. Type 'bye' to exit the chat.

## Code Structure

The program is structured as follows:

- **responses**: A dictionary containing predefined rules and corresponding lists of responses.
- **get_response(user_input)**: A function that generates a response based on the user's input by checking against the predefined rules.
- **Main chat loop**: A loop where the user can interact with the chatbot. It prints the initial greeting and waits for user input. The loop continues until the user types 'bye'.

## Customization

Feel free to customize the `responses` dictionary to add or modify rules and responses according to your preferences. You can enhance the chatbot by expanding the set of predefined rules and responses.

## Example

```python
# Sample interaction with the chatbot
Chatbot: Hi! How can I help you today? (Type 'bye' to exit)
You: What's your name?
Chatbot: you can call me JOI.
You: How are you doing?
Chatbot: I'm just a chatbot. I don't have feelings, but I'm here to help.
You: Bye
Chatbot: Goodbye!
```

## Contributors


Feel free to contribute to the project by enhancing the code or adding new features. If you find any issues or have suggestions for improvement, please create an issue on the [GitHub repository](https://github.com/yourusername/joi-chatbot).

Thank you for using JOI Chatbot!
