# DNA

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 6 - DNA Problem Set](https://cs50.harvard.edu/x/2023/psets/6/dna/). This Python program analyzes a given DNA sequence and identifies to whom it belongs based on the counts of Short Tandem Repeats (STRs). It compares the STR counts in the DNA sequence with those in a CSV database containing the STR profiles of different individuals. If a match is found, the program outputs the name of the matching individual.

## Getting Started

1. Ensure you have Python installed on your machine.
2. Download the program files by running the following commands in your terminal:

    ```bash
    cd dna
    ```

3. Run the program by executing the command `python dna.py`.

## Program Structure

- `dna.py`: The main Python program that reads the DNA sequence and the database, computes the longest match of each STR in the DNA sequence, and identifies to whom the DNA belongs.

## Usage

1. Open a terminal and navigate to the `dna` directory.
2. Run the program using the command `python dna.py [database_file] [sequence_file]`, where `[database_file]` is the CSV file containing STR profiles, and `[sequence_file]` is the text file containing the DNA sequence to identify.

## How the Program Works

1. The program checks for the correct number of command-line arguments. If incorrect, it displays an error message and exits.
2. The program reads the CSV database file and the DNA sequence file into memory.
3. For each STR in the database, the program uses a helper function, `longest_match`, to compute the longest consecutive sequence of repeats in the DNA sequence.
4. It then compares the computed STR counts with those in the database to find a matching profile.
5. If a match is found, the program outputs the name of the individual. Otherwise, it outputs "No match".

## Testing

You can test the program by running it with different database and sequence files. For example:

```bash
$ python dna.py databases/large.csv sequences/5.txt
Lavender
```

## Additional Notes

- The program utilizes CSV and text file reading functionalities to process the DNA sequence and database files.
- It calculates the longest consecutive sequence of repeats for each STR in the DNA sequence.
- The program identifies the person whose STR counts match those in the database.
- This program provides insights into DNA profiling and sequence matching using STRs.
- Keep in mind that this program is a simplified example to showcase DNA sequence matching concepts in programming.

Remember to use actual file paths for the `[database_file]` and `[sequence_file]` arguments when running the program.