# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman word-guessing game to practice Python strings, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Choose a Word and Show Progress

#### Description
Create the starting state for a Hangman game by selecting a secret word and showing which letters the player has guessed correctly.

#### Requirements
Completed program should:

- Select a secret word at random from a predefined list.
- Display one underscore for each letter in the secret word.
- Ask the player to enter a letter and reveal matching letters in their correct positions.

### 🛠️ Track Guesses and Finish the Game

#### Description
Add a game loop that tracks incorrect guesses and ends when the player either guesses the word or runs out of attempts.

#### Requirements
Completed program should:

- Give the player a limited number of incorrect guesses and decrease the remaining attempts for each incorrect guess.
- Display the updated word progress and remaining attempts after each guess.
- End when the word is fully revealed or no attempts remain.
- Display a win message when the player guesses the word and a lose message when attempts run out.
