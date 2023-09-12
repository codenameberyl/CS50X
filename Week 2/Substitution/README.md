# Substitution

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 2 - Substitution Problem Set](https://cs50.harvard.edu/x/2023/psets/2/substitution/). The `substitution` program encrypts messages using a substitution cipher, a technique that replaces each letter in the plaintext with a corresponding letter from a predefined key. This program accepts a single command-line argument, which is the key used for the substitution. The user is then prompted to input the plaintext message, and the program outputs the corresponding ciphertext.

## Getting Started

To get started with the `substitution` program, follow these steps:

1. **Download the Source Code**: If you haven't already, download the source code for the `substitution` problem set by using the provided link and extracting the contents of the ZIP file. You should now have a file named `substitution.c`.

2. **Compile the Program**: Open a terminal and navigate to the directory where the `substitution.c` file is located. Compile the program using a C compiler (e.g., `gcc`) with the following command:

   ```
   gcc -o substitution substitution.c -lcs50
   ```

3. **Run the Program**: Execute the compiled program by typing `./substitution` followed by the substitution key in the terminal.

## Usage

When you run the `substitution` program, it will prompt you to input a plaintext message. After you provide the message, the program will encrypt it using a substitution cipher with the specified key and print the corresponding ciphertext.

## Examples

Here are a few examples of how the program might work:

1. Encrypting with a key of "YTNSHKVEFXRBAUQZCLWDMIPGJO":

   ```
   $ ./substitution YTNSHKVEFXRBAUQZCLWDMIPGJO
   plaintext:  HELLO
   ciphertext: EHBBQ
   ```

2. Encrypting with a key of "VCHPRZGJNTLSKFBDQWAXEUYMOI":

   ```
   $ ./substitution VCHPRZGJNTLSKFBDQWAXEUYMOI
   plaintext:  hello, world
   ciphertext: jrssb, ybwsp
   ```

3. Handling an invalid key:

   ```
   $ ./substitution ABC
   Key must contain 26 characters.
   ```

4. Providing an incorrect number of arguments:

   ```
   $ ./substitution
   Usage: ./substitution key
   ```

   ```
   $ ./substitution 1 2 3
   Usage: ./substitution key
   ```

## Notes

- The program uses the `cs50.h` library for input and string manipulation functions.

- The `is_valid_key` function checks whether a given key is valid according to the rules specified in the problem description.

- The `encrypt` function performs the encryption by substituting each character in the plaintext with the corresponding character in the key.

- The program preserves the case of the original message. Capitalized letters remain capitalized, and lowercase letters remain lowercase.

- The program prompts the user for a plaintext message after providing the substitution key.

- The program prints the ciphertext after prompting for input.

## How to Test

You can test the program by providing different plaintext messages and substitution keys. Compare the ciphertext output with the expected results based on the substitution cipher encryption rules.