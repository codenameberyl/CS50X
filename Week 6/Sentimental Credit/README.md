# Sentimental / Credit

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 6 - Sentimental / Credit Problem Set](https://cs50.harvard.edu/x/2023/psets/6/credit/). This Python program validates credit card numbers using Luhn's algorithm and determines whether they belong to American Express, MasterCard, or Visa. The program prompts the user for a credit card number and prints the result accordingly.

## Getting Started

1. Make sure you have Python installed on your machine.
2. Download the program files by running the following commands in your terminal:

    ```bash
    cd "Sentimental / Credit"
    ```

3. Run the program by executing the command `python credit.py`.

## Program Structure

- `credit.py`: The main Python program that prompts the user for a credit card number, validates it using Luhn's algorithm, and identifies the card type.

## Usage

1. Open a terminal and navigate to the `"Sentimental / Credit"` directory.
2. Run the program using the command `python credit.py`.
3. Follow the prompts to input a credit card number.

## How the Program Works

1. The program uses a `while` loop to continuously prompt the user for input until a valid credit card number is provided.
2. Inside the loop, the program attempts to read the user's input using the `input` function.
3. The program then checks if the provided credit card number is valid by applying Luhn's algorithm. The algorithm involves summing up the digits of the card number and checking if the sum is divisible by 10.
4. After validating the card number, the program checks its length and starting digits to determine whether it belongs to American Express, MasterCard, or Visa.
5. The program prints the result (AMEX, MASTERCARD, VISA, or INVALID) based on the validation and identification process.

## Testing

You can test the program by running it and providing different credit card numbers. For example:

```bash
$ python credit.py
Number: 378282246310005
AMEX
```

## Additional Notes

- The program uses Luhn's algorithm to validate the credit card number.
- The program checks the length and starting digits of the card number to identify the card type.
- The program ensures that the user's input consists of digits only.
- Remember that this program is a simplified example for demonstrating input validation, algorithmic processing, and output formatting in Python. It serves as a starting point for understanding these concepts in programming.