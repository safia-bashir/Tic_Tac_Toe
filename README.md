# Tic_Tac_Toe
# Tic-Tac-Toe Game in Python

## Introduction
Tic-Tac-Toe is a classic and popular game known for its simplicity and entertainment. It is a two-player game where players take turns to mark the spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. If the grid is filled and no player has won, the game is a draw.

## Algorithm
We will now discuss the algorithm to write the code. This algorithm will help you to write code in any programming language of your choice. Here’s how it’s done:

### 1. Initialize the Game Board
   - Create a 3x3 game board, initializing each spot with "-".

### 2. Decide the First Player
   - Randomly decide which player goes first.

### 3. Display the Board
   - Create a function to display the current state of the board.

### 4. Player Turn and Input
   - In each turn, prompt the current player to enter the row and column numbers where they want to place their marker.

### 5. Mark the Spot
   - After validating the input, mark the chosen spot on the board with the current player's marker.

### 6. Check for Win or Draw
   - After each turn, check if the current player has won or if the game is a draw.

### 7. Swap Players
   - After each turn, swap the current player for the next turn.

### 8. Repeat Steps 3-7
   - Continue repeating steps 3-7 until there is a winner or the board is full, resulting in a draw.

### 9. End the Game
   - Once the game has ended, display the final state of the board and a message declaring the result of the game.

## Pseudocode
```plaintext
Initialize the game board as a 3x3 matrix filled with "-"
While the game is not over:
    Display the board
    Prompt the current player to enter row and column numbers
    Validate the input
    If the input is valid:
        Mark the chosen spot with the current player's marker
        Check for a win or a draw
        If there is a winner or the game is a draw:
            Declare the result and end the game
        Else:
            Swap players and continue to the next turn
