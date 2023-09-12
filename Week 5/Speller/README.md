# Speller

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 5 - Speller Problem Set](https://cs50.harvard.edu/x/2023/psets/5/speller/). This is a spell checker program that utilizes a hash table to efficiently check the spelling of words in a given text file. It implements a basic version of a dictionary that allows you to load words into memory, check for the correct spelling of words, determine the number of words in the dictionary, and unload the dictionary when it's no longer needed. The spell checker is case-insensitive and can handle words with apostrophes.

## Usage

To use the spell checker, follow these steps:

1. Compile the program by executing `make speller` in the terminal.
2. Run the program with the following syntax:
   ```
   ./speller [DICTIONARY] text
   ```
   - `DICTIONARY` (optional): Specify the path to the dictionary file. Default is `"dictionaries/large"`.
   - `text`: Specify the path to the text file you want to spell-check.

## Features

- Case-insensitive spell checking: The spell checker treats words with different capitalizations as equivalent.
- Fast execution: The program is designed to be efficient and minimize execution time for loading, checking, and unloading words.
- Hash table implementation: The program uses a hash table to store and quickly access dictionary words.
- Memory management: The program ensures memory allocated during the loading phase is properly released during unloading.
- Benchmarking: The program reports time spent in loading, checking, determining size, and unloading the dictionary.

## Files

- `speller.c`: Implements the main logic of the spell checker, including loading, checking, and unloading words.
- `dictionary.c`: Implements functions for loading, checking, determining size, and unloading the dictionary.
- `dictionary.h`: Contains function prototypes for dictionary operations and necessary constants.
- `Makefile`: Used for automating the compilation process.
- `texts/`: Contains sample text files for testing the spell checker.
- `keys/`: Contains answer keys that list the expected misspelled words in the sample texts.
- `README.md`: This file.

## How It Works

1. **load**: Reads words from the dictionary file and stores them in a hash table.
2. **hash**: Calculates a hash value for a given word to determine the index in the hash table.
3. **size**: Counts the number of words in the dictionary by traversing the hash table.
4. **check**: Hashes a word and checks if it exists in the dictionary by looking up the hash table.
5. **unload**: Frees the memory used by the hash table and its nodes.

## Performance

The program aims to minimize execution time for dictionary operations while maintaining reasonable memory usage. By using a hash table, the spell checker achieves faster lookups compared to linear search through a large dictionary.

## Testing

You can test the speller on various text files located in the `texts/` directory. Compare the program's output with the answer keys in the `keys/` directory to validate the correctness of the spell checker.