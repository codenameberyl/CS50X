# Sentimental / Cash

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 6 - Sentimental / Cash Problem Set](https://cs50.harvard.edu/x/2023/psets/6/cash/). This Python program calculates the minimum number of coins required to give a user change using quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢). The program prompts the user for the amount of change owed and then calculates and prints the minimum number of coins needed to make that change.

## Getting Started

1. Make sure you have Python installed on your machine.
2. Download the program files by running the following commands in your terminal:

    ```bash
    cd "Sentimental / Cash"
    ```

3. Run the program by executing the command `python cash.py`.

## Program Structure

- `cash.py`: The main Python program that prompts the user for the amount of change owed, calculates the minimum number of coins, and prints the result.

## Usage

1. Open a terminal and navigate to the `"Sentimental / Cash"` directory.
2. Run the program using the command `python cash.py`.
3. Follow the prompts to input the amount of change owed.

## How the Program Works

1. The program uses a `while` loop to continuously prompt the user for input until a valid input is provided.
2. Inside the loop, the program attempts to convert the user's input to a floating-point number using the `float` function.
3. If the conversion is successful and the input is greater than 0, the program proceeds to calculate the minimum number of coins needed.
4. The program multiplies the user's input by 100 and rounds it to convert the amount to cents.
5. It then calculates the number of quarters, dimes, nickels, and pennies needed using integer division and the modulo operator.
6. The total count of coins is calculated by adding up the counts of each type of coin.
7. The program prints the total count of coins as the result.

## Testing

You can test the program by running it and providing different amounts of change owed. For example:

```bash
$ python cash.py
Change owed: 0.41
4
```

## Additional Notes

- The program ensures that the user's input is greater than 0 before proceeding to calculate the coins.
- The program calculates the number of each type of coin needed using integer division and the modulo operator.
- The total count of coins needed is calculated by adding up the counts of quarters, dimes, nickels, and pennies.
- The program converts the user's input into cents for accurate calculations.
- Feel free to experiment with the program by providing different input values to see how it calculates the minimum number of coins required.

Remember that this program is a simple example to demonstrate input validation, calculations, and output formatting in Python. It's a starting point to learn about these concepts in programming.