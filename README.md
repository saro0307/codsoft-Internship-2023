# codsoft-Internship-2023

# Movie Recommendation System

## Overview

This R script provides a simple movie recommendation system based on cosine similarity between movie descriptions. The program uses the "tm" and "proxy" packages to process text data and calculate similarity scores.

## Installation

Before running the script, make sure to install the required R packages. You can do this by running the following commands in your R environment:

```R
if (!require("tm")) install.packages("tm", dependencies=TRUE)
if (!require("proxy")) install.packages("proxy", dependencies=TRUE)
```

After installing the packages, load them using:

```R
library(tm)
library(proxy)
```

## Usage

1. Define your movie dataset with titles and descriptions.
2. Create a corpus and document-term matrix (DTM) from the movie descriptions.
3. Compute cosine similarity between movie descriptions.
4. Use the `get_recommendations` function to get movie recommendations based on a user's preference.

Example:

```R
# Example usage:
user_preference <- "The Shawshank Redemption"
recommendations <- get_recommendations(user_preference)
cat("Recommended movies for", user_preference, ":\n", recommendations, "\n")
```

## Functionality

The program includes the following functionality:

- **Loading Packages:** The script checks for the presence of required packages and installs them if necessary.
- **Data Preparation:** A dataset of movies is provided as an example, but you can replace it with your own dataset.
- **Cosine Similarity:** The script calculates cosine similarity between movie descriptions using a document-term matrix.
- **Recommendation Function:** The `get_recommendations` function takes a movie title as input and returns a list of recommended movies based on similarity scores.

Feel free to customize the script and adapt it to your own movie dataset.

## License

This program is licensed under the [MIT License](LICENSE). You are free to modify and distribute the code for personal or commercial use. See the [LICENSE](LICENSE) file for details.

## Contributors

If you have any suggestions or improvements, feel free to contribute to the project.

Happy movie recommending!



# JOI Chatbot

## Description
This is a simple Python chatbot program that responds to user input based on predefined rules. The chatbot uses a set of rules and responses to generate replies. It's designed to engage in basic conversations and provide default responses when specific rules are not matched.

## Usage
1. Ensure you have Python installed on your system.
2. Download the `chatbot.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `chatbot.py` file is located.
5. Run the program using the command: `python chatbot.py`

The chatbot will initiate a conversation, and you can type your messages to interact with it. To exit the chat, simply type 'bye.'

## Predefined Rules and Responses
The chatbot recognizes specific rules and provides corresponding responses. Here are some examples:

- **Greetings:**
  - Input: "hello"
  - Response: Random greeting from ["Hello!", "Hi there!", "Hey!"]

- **Inquiry about well-being:**
  - Input: "how are you"
  - Response: Random response from ["I'm just a chatbot.", "I don't have feelings, but I'm here to help."]

- **Name inquiry:**
  - Input: "what's your name"
  - Response: "You can call me JOI."

- **Farewell:**
  - Input: "bye"
  - Response: Random farewell message from ["Goodbye!", "See you later!", "Bye!"]

- **Default responses:**
  - If no specific rule matches, the chatbot provides a default response from ["I'm not sure I understand.", "Can you please rephrase that?", "I don't have an answer for that."]

## License
This chatbot program is distributed under the [MIT License](LICENSE).

## Disclaimer
This chatbot is a basic example and may not handle complex conversations or understand nuanced queries. It is recommended for educational purposes and may be enhanced for more sophisticated use cases. Use at your own discretion.



# Tic-Tac-Toe Game

This simple Python program allows you to play Tic-Tac-Toe against an AI opponent that uses the Minimax algorithm to make optimal moves.

## How to Play

1. Run the program.
2. The Tic-Tac-Toe board will be displayed, and you will play as "X" while the AI plays as "O".
3. Enter your move by typing a number from 0 to 8, representing the position on the board where you want to place your "X".
4. The AI will then make its move.
5. The game continues until one player wins or the board is full, resulting in a tie.

## Code Overview

- The Tic-Tac-Toe board is represented as a list with 9 elements.
- The `print_board` function prints the current state of the board.
- The `check_winner` function checks if a player has won.
- The `is_board_full` function checks if the board is full.
- The `minimax` function implements the Minimax algorithm for the AI player.
- The `find_best_move` function finds the best move for the AI using the Minimax algorithm.
- The main game loop alternates between the human player and the AI until the game is over.

## How the AI Works

The AI uses the Minimax algorithm, a decision-making algorithm that evaluates all possible moves to choose the one that maximizes its chances of winning or minimizes its chances of losing. It recursively explores all possible game states to determine the optimal move.

## Running the Program

To run the program, ensure you have Python installed on your system. Execute the script, and the game will start in the console.

```bash
python tic_tac_toe.py
```

## License

This Tic-Tac-Toe program is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify, enhance, or share this program! Have fun playing Tic-Tac-Toe!
