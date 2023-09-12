# Sentimental / Readability

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 6 - Sentimental / Readability Problem Set](https://cs50.harvard.edu/x/2023/psets/6/readability/). This Python program analyzes the readability of a given text using the Coleman-Liau formula. It prompts the user to input some text and then calculates the approximate grade level required to comprehend the text. The program takes into account the average number of letters, words, and sentences in the text to determine its readability.

## Getting Started

1. Ensure you have Python installed on your machine.
2. Download the program files by running the following commands in your terminal:

    ```bash
    cd "Sentimental / Readability"
    ```

3. Run the program by executing the command `python readability.py`.

## Program Structure

- `readability.py`: The main Python program that prompts the user for input, calculates the readability score, and determines the corresponding grade level.

## Usage

1. Open a terminal and navigate to the `"Sentimental / Readability"` directory.
2. Run the program using the command `python readability.py`.
3. Follow the prompts to input the text you want to analyze.

## How the Program Works

1. The program prompts the user for input using the `input` function.
2. It calculates the average number of letters, words, and sentences in the provided text.
3. The program then applies the Coleman-Liau formula: `0.0588 * L - 0.296 * S - 15.8`, where `L` is the average number of letters per 100 words, and `S` is the average number of sentences per 100 words.
4. The calculated index is rounded to the nearest integer to determine the approximate grade level required to comprehend the text.
5. Depending on the calculated grade level, the program prints "Before Grade 1", "Grade 16+", or the actual grade level.

## Testing

You can test the program by running it and providing different texts. For example:

```bash
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

## Additional Notes

- The program calculates the readability of the input text based on the average number of letters, words, and sentences.
- It uses the Coleman-Liau formula to determine the approximate grade level.
- The program provides readability insights for various texts, indicating the grade level required to comprehend them.
- Remember that this program is a simplified example for demonstrating text analysis and algorithmic processing in Python. It serves as a starting point for understanding these concepts in programming.