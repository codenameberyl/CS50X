# Sentimental / Mario (Less)

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 6 - Sentimental / Mario (Less) Problem Set](https://cs50.harvard.edu/x/2023/psets/6/mario/less/). This Python program generates a half-pyramid of a specified height using hash symbols (#). The program prompts the user to provide the height of the pyramid and then generates the pyramid according to the user's input.

## Getting Started

1. Make sure you have Python installed on your machine.
2. Download the program files by running the following commands in your terminal:

    ```bash
    cd "Sentimental / Mario (Less)"
    ```

3. Run the program by executing the command `python mario.py`.

## Program Structure

- `mario.py`: The main Python program that prompts the user for the height of the pyramid and generates the half-pyramid using hash symbols.

## Usage

1. Open a terminal and navigate to the `"Sentimental / Mario (Less)"` directory.
2. Run the program using the command `python mario.py`.
3. Follow the prompts to input the desired height of the half-pyramid.

## How the Program Works

1. The program uses a `while` loop to continuously prompt the user for input until a valid input is provided.
2. Inside the loop, the program attempts to convert the user's input to an integer using the `int` function.
3. If the conversion is successful and the input is within the range of 1 to 8 (inclusive), the program enters a nested loop to generate the half-pyramid.
4. The nested loop uses the `print` function to display spaces and hash symbols, creating the pattern of the half-pyramid.
5. The number of spaces and hash symbols printed in each line is determined by the current value of the loop variables.
6. If the user's input is not valid (not a positive integer between 1 and 8), the program continues to prompt the user for input.

## Testing

You can test the program by running it and providing different height values as input. For example:

```bash
$ python mario.py
Height: 4
   #
  ##
 ###
####
```

## Additional Notes

- The program uses a `try` and `except` block to handle cases where the user's input cannot be converted to an integer (ValueError).
- The program ensures that the height input is within a valid range (1 to 8) before generating the half-pyramid.
- The program uses the `print` function to display spaces and hash symbols. The number of spaces and hash symbols in each line is determined by the loop variables.
- Feel free to experiment with the program by adjusting the range of valid heights or customizing the symbols used to build the half-pyramid.

Remember that this program is a simple example to demonstrate user input, loops, and output formatting in Python. It's a starting point to learn about these concepts in programming.