# Bulbs

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 2 - Bulbs Problem Set](https://cs50.harvard.edu/x/2023/psets/2/bulbs/). The `bulbs` program converts a given message into a series of instructions for a strip of bulbs on stage. Each character in the message is first converted to its ASCII value and then further converted into an 8-bit binary number. The program then prints a sequence of emojis representing light bulbs, using yellow and black emojis to indicate on and off states respectively.

## Getting Started

To get started with the `bulbs` program, follow these steps:

1. **Download the Source Code**: If you haven't already, download the source code for the `bulbs` problem set by using the provided link and extracting the contents of the ZIP file. You should now have a file named `bulbs.c`.

2. **Compile the Program**: Open a terminal and navigate to the directory where the `bulbs.c` file is located. Compile the program using a C compiler (e.g., `gcc`) with the following command:

   ```
   gcc -o bulbs bulbs.c -lcs50
   ```

3. **Run the Program**: Execute the compiled program by typing `./bulbs` in the terminal.

## Usage

When you run the `bulbs` program, it will prompt you to input a message. After you provide the message, the program will convert each character in the message to an 8-bit binary number and print a sequence of emojis representing light bulbs. Each byte of 8 symbols will be printed on its own line, and a newline will also be added after each byte.

## Example

Here's an example of how the `bulbs` program works:

```
$ ./bulbs
Message: HI!
⚫🟡⚫⚫🟡⚫⚫⚫
⚫🟡⚫⚫🟡⚫⚫🟡
⚫⚫🟡⚫⚫⚫⚫🟡
```

```
# ./bulbs
Message: HI MOM
⚫🟡⚫⚫🟡⚫⚫⚫
⚫🟡⚫⚫🟡⚫⚫🟡
⚫⚫🟡⚫⚫⚫⚫⚫
⚫🟡⚫⚫🟡🟡⚫🟡
⚫🟡⚫⚫🟡🟡🟡🟡
⚫🟡⚫⚫🟡🟡⚫🟡
```

In the example above, the user inputs the message "HI!", and the program converts each character to an 8-bit binary number and prints the corresponding emojis to represent light bulbs. The yellow emoji represents an on state, and the black emoji represents an off state.

## Notes

- The program uses the `cs50.h` library for input and string manipulation functions.

- The `print_bulb` function is provided to print the appropriate emoji for each bit (0 or 1).

- The program converts each character in the message to its ASCII value and then further converts the ASCII value into an 8-bit binary number. Each bit of the binary number corresponds to an emoji representing a light bulb.

- The program prints each byte of 8 symbols on a separate line to improve readability.

- The program's behavior follows the provided examples, converting characters to their binary representations and displaying them using emojis.

## How to Test

You can test the program by providing different messages and observing the sequence of emojis printed for each character. Use the provided examples to verify that the program produces the correct sequence of emojis for different messages.