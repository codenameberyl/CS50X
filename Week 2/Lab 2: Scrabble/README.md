# Lab 2: Scrabble

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 2 - Lab 2: Scrabble](https://cs50.harvard.edu/x/2023/labs/2/). The `scrabble` program is a simple implementation that determines the winner of a Scrabble-like game between two players. Each player enters a word, and the program calculates the score for each word based on the point values of individual letters. The player with the higher score wins the game.

## Getting Started

To get started with the `scrabble` program, follow these steps:

1. **Download the Source Code**: If you haven't already, download the source code for the `scrabble` lab by using the provided link and extracting the contents of the ZIP file. You should now have a file named `scrabble.c`.

2. **Compile the Program**: Open a terminal and navigate to the directory where the `scrabble.c` file is located. Compile the program using a C compiler (e.g., `gcc`) with the following command:

   ```
   gcc -o scrabble scrabble.c -lcs50
   ```

3. **Run the Program**: Execute the compiled program by typing `./scrabble` in the terminal.

## Usage

When you run the `scrabble` program, it will prompt both players to enter their respective words. After both words have been entered, the program will calculate the scores for each word and determine the winner of the game. The player with the higher score wins, and the program will output the result as either "Player 1 wins!", "Player 2 wins!", or "Tie!".

## Example

Here's an example of how the `scrabble` program works:

```
$ ./scrabble
Player 1: Question?
Player 2: Question!
Tie!
```

```
$ ./scrabble
Player 1: Oh,
Player 2: hai!
Player 2 wins!
```

```
$ ./scrabble
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

```
$ ./scrabble
Player 1: Scrabble
Player 2: wiNNeR
Player 1 wins!
```

## Testing

You can test the program by providing different words with varying lengths and letter combinations to see how the program calculates the scores and determines the winner. Experiment with both lowercase and uppercase letters to observe the behavior of the program.

## Notes

- The program uses an array named `POINTS` to store the point values of each letter of the alphabet.
- The `compute_score()` function calculates the score for a given word based on the letter point values specified in the `POINTS` array.
- The program utilizes the `cs50.h` library for input and string manipulation functions.