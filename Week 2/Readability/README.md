# Readability

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 2 - Readability Problem Set](https://cs50.harvard.edu/x/2023/psets/2/readability/). The `readability` program calculates the approximate grade level needed to comprehend a given text using the Coleman-Liau index. The Coleman-Liau index is a formula that computes the reading level based on the average number of letters, words, and sentences in the text.

## Getting Started

To get started with the `readability` program, follow these steps:

1. **Download the Source Code**: If you haven't already, download the source code for the `readability` problem set by using the provided link and extracting the contents of the ZIP file. You should now have a file named `readability.c`.

2. **Compile the Program**: Open a terminal and navigate to the directory where the `readability.c` file is located. Compile the program using a C compiler (e.g., `gcc`) with the following command:

   ```
   gcc -o readability readability.c -lcs50 -lm
   ```

3. **Run the Program**: Execute the compiled program by typing `./readability` in the terminal.

## Usage

When you run the `readability` program, it will prompt you to input a text. After you provide the text, the program will calculate the Coleman-Liau index for the text and determine its approximate grade level. The program will then output the grade level of the text.

## Example

Here's an example of how the `readability` program works:

```
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

In this example, the user inputs a text, and the program calculates the Coleman-Liau index for the text. Based on the index, the program determines that the text is at a third-grade reading level.

## Notes

- The program uses the Coleman-Liau formula to compute the grade level of the text. The formula takes into account the average number of letters, words, and sentences in the text.

- The program uses the `cs50.h` library for input and string manipulation functions and the `math.h` library for rounding operations.

- The program handles various sentence-ending punctuations such as periods, exclamation points, and question marks to determine the number of sentences.

- If the calculated index is 16 or higher, the program outputs "Grade 16+" to indicate a senior undergraduate reading level. If the index is less than 1, the program outputs "Before Grade 1".

Remember to compile and run the program using the provided instructions to see how the program calculates the grade level of different texts.

## How to Test

You can test the program by providing different texts and observing the calculated grade levels. Use the provided example texts to verify that the program produces the correct results for different reading levels.