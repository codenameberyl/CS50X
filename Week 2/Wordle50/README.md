# Wordle50

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 2 - Wordle50 Problem Set](https://cs50.harvard.edu/x/2023/psets/2/wordle50/). The `wordle` program is a terminal-based word game inspired by the popular Wordle daily word game. In this game, the player needs to guess a secret word within a certain number of tries. The game provides feedback on each guess by color-coding the guessed letters based on their correctness and position.

## Getting Started

To get started with the `wordle` program, follow these steps:

1. **Download the Source Code**: Download the source code for the `wordle` problem set using the provided link and extract the contents of the ZIP file. You will find a file named `wordle.c` in the extracted folder.

2. **Compile the Program**: Open a terminal and navigate to the directory where the `wordle.c` file is located. Compile the program using a C compiler (e.g., `gcc`) with the following command:

   ```
   gcc -o wordle wordle.c -lcs50
   ```

3. **Run the Program**: Execute the compiled program by typing `./wordle` followed by the desired word size (5, 6, 7, or 8) in the terminal.

## Usage

When you run the `wordle` program, you need to provide a single command-line argument, which is the desired word size (number of letters) you want to guess. The program will prompt you to input a word guess of the specified size. After each guess, the program will provide feedback on the guessed word by color-coding the letters based on their correctness and position. The game continues until you guess the correct word or exhaust your allowed number of guesses.

## Examples

Here are a few examples of how the program might work:

1. Starting a game with a word size of 5:

   ```
   $ ./wordle 5
   This is WORDLE50
   You have 6 tries to guess the 5-letter word I'm thinking of
   Input a 5-letter word: crash
   Guess 1: crash
   Input a 5-letter word: scone
   Guess 2: scone
   Input a 5-letter word: since
   Guess 3: since
   You won!
   ```

2. Guessing the wrong word:

   ```
   $ ./wordle 6
   This is WORDLE50
   You have 7 tries to guess the 6-letter word I'm thinking of
   Input a 6-letter word: gaming
   Guess 1: gamin# guess is color-coded here
   Input a 6-letter word: crazy#
   Guess 2: cra#y guess is color-coded here
   ...
   Sorry, you lost. The word was effect.
   ```

## Notes

- The program uses the `cs50.h` library for input and string manipulation functions.

- The game provides color-coded feedback for each guessed letter:
  - Green letters represent correct letters in the correct position.
  - Yellow letters represent correct letters in the wrong position.
  - Red letters represent incorrect letters.

- The game continues for a certain number of guesses (equal to the word size + 1).

- The program selects a secret word from a pre-defined list of words of the specified length.

## How to Test

You can test the program by providing word guesses of various lengths and observing the color-coded feedback. Try guessing both correct and incorrect words to see how the program responds.