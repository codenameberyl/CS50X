# Caesar

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 2 - Caesar Problem Set](https://cs50.harvard.edu/x/2023/psets/2/caesar/). The `caesar` program encrypts messages using Caesar's cipher, a simple encryption technique where each letter in the plaintext is shifted by a certain number of positions in the alphabet. This program accepts a single command-line argument, which is a non-negative integer representing the key for the encryption. The user is then prompted to input the plaintext message, and the program outputs the corresponding ciphertext.

## Getting Started

To get started with the `caesar` program, follow these steps:

1. **Download the Source Code**: If you haven't already, download the source code for the `caesar` problem set by using the provided link and extracting the contents of the ZIP file. You should now have a file named `caesar.c`.

2. **Compile the Program**: Open a terminal and navigate to the directory where the `caesar.c` file is located. Compile the program using a C compiler (e.g., `gcc`) with the following command:

   ```
   gcc -o caesar caesar.c -lcs50
   ```

3. **Run the Program**: Execute the compiled program by typing `./caesar` followed by the encryption key in the terminal.

## Usage

When you run the `caesar` program, it will prompt you to input a plaintext message. After you provide the message, the program will encrypt it using Caesar's cipher with the specified key and print the corresponding ciphertext.

## Examples

Here are a few examples of how the program might work:

1. Encrypting with a key of 1:

   ```
   $ ./caesar 1
   plaintext:  HELLO
   ciphertext: IFMMP
   ```

2. Encrypting with a key of 13:

   ```
   $ ./caesar 13
   plaintext:  hello, world
   ciphertext: uryyb, jbeyq
   ```

3. Handling non-digit arguments:

   ```
   $ ./caesar banana
   Usage: ./caesar key
   ```

   ```
   $ ./caesar 1 2 3
   Usage: ./caesar key
   ```

## Notes

- The program uses the `cs50.h` library for input and string manipulation functions.

- The `only_digits` function checks whether a given string contains only digits (0-9).

- The `rotate` function implements the Caesar cipher encryption. It takes a character and a key as input, and returns the rotated character.

- The program preserves the case of the original message. Capitalized letters remain capitalized, and lowercase letters remain lowercase.

- The program prompts the user for a plaintext message after providing the encryption key.

- The program prints the ciphertext after prompting for input.

## How to Test

You can test the program by providing different plaintext messages and encryption keys. Compare the ciphertext output with the expected results based on the Caesar cipher encryption rules.