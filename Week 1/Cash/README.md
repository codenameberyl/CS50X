# Cash

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 1 - Cash Problem Set](https://cs50.harvard.edu/x/2023/psets/1/cash/). The `cash` program is a simple implementation of a greedy algorithm used to calculate the minimum number of coins required to provide change to a customer. It prompts the user for the amount of change owed and then calculates the smallest number of coins needed to make up that amount using quarters, dimes, nickels, and pennies.

## Getting Started

To get started with the `cash` program, follow these steps:

1. **Download the Source Code**: If you haven't already, download the source code for the `cash` problem by using the provided link and extracting the contents of the ZIP file. You should now have a file named `cash.c`.

2. **Compile the Program**: Open a terminal and navigate to the directory where the `cash.c` file is located. Compile the program using a C compiler (e.g., `gcc`) with the following command:

   ```
   make cash
   ```

3. **Run the Program**: Execute the compiled program by typing `./cash` in the terminal.

## Usage

When you run the `cash` program, it will prompt you for the amount of change owed in cents. You can enter a positive integer representing the amount of change. If you enter a negative value or a non-integer value, the program will re-prompt you until you enter a valid input.

After you provide the change owed, the program will calculate and display the minimum number of coins required to make up that amount using quarters, dimes, nickels, and pennies.

## Example

Here's an example of how the `cash` program works:

```
$ ./cash
Change owed: 41
4
```

In this example, the user owes 41 cents in change, and the program calculates that the smallest number of coins needed is 4 (1 quarter, 1 dime, 1 nickel, and 1 penny).

## Testing

You can test the program by providing different amounts of change owed and verifying that the calculated output matches your expectations. Try inputting negative values, zero, positive integers, and non-integer values to see how the program responds.

## Notes

- The program uses the `cs50.h` library.
- The `get_cents` function is responsible for prompting the user for the amount of change owed and validating the input.
- The `calculate_quarters`, `calculate_dimes`, `calculate_nickels`, and `calculate_pennies` functions calculate the number of each coin type needed based on the amount of change owed.