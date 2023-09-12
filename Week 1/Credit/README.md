# Credit

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 1 - Credit Problem Set](https://cs50.harvard.edu/x/2023/psets/1/credit/). The `credit` program is a simple implementation of Luhn's algorithm for validating credit card numbers and determining their issuer (American Express, MasterCard, or Visa). It prompts the user for a credit card number, performs the necessary calculations, and outputs the type of credit card or "INVALID" if the number is not valid.

## Getting Started

To get started with the `credit` program, follow these steps:

1. **Download the Source Code**: If you haven't already, download the source code for the `credit` problem by using the provided link and extracting the contents of the ZIP file. You should now have a file named `credit.c`.

2. **Compile the Program**: Open a terminal and navigate to the directory where the `credit.c` file is located. Compile the program using a C compiler (e.g., `gcc`) with the following command:

   ```
   make credit
   ```

3. **Run the Program**: Execute the compiled program by typing `./credit` in the terminal.

## Usage

When you run the `credit` program, it will prompt you for a credit card number. You can enter a positive integer representing the credit card number without any hyphens or other separators. The program will then perform the necessary calculations to determine if the number is valid and, if so, what type of credit card it is (AMEX, MASTERCARD, or VISA).

The program's output will be one of the following:

- If the credit card number is valid American Express: AMEX
- If the credit card number is valid MasterCard: MASTERCARD
- If the credit card number is valid Visa: VISA
- If the credit card number is not valid: INVALID

## Example

Here's an example of how the `credit` program works:

```
$ ./credit
Number: 4003600000000014
VISA
```

In this example, the user enters the credit card number 4003600000000014. The program calculates that the credit card is a Visa card and outputs "VISA."

## Testing

You can test the program by providing different credit card numbers, both valid and invalid, to see how the program responds. Try using different lengths of credit card numbers and different starting digits to test the different credit card types (AMEX, MASTERCARD, VISA), as well as invalid card numbers.

## Notes

- The program uses the `cs50.h` library.
- The program uses Luhn's algorithm to validate the credit card number.
- The program checks the length of the credit card number and the first few digits to determine the type of credit card.