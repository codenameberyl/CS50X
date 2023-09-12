# Runoff

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 3 - Runoff Problem Set](https://cs50.harvard.edu/x/2023/psets/3/runoff/). The "Runoff" program simulates a ranked-choice voting system known as an instant runoff system. In this system, voters can rank candidates in order of preference, and the program determines the winner based on these preferences.

## Getting Started

To get started with the program, follow these steps:

1. **Download the Source Code**: Download the source code for the program using the provided link and extract the contents of the ZIP file. You will find a file named `runoff.c`.

2. **Navigate to the Program Directory**: Open a terminal and navigate to the directory where the `runoff.c` file is located. You can do this by using the `cd` command.

   ```
   cd path/to/runoff-directory
   ```

3. **Compile the Program**: Compile the `runoff.c` file to create the executable program. Use the following command:

   ```
   clang -o runoff runoff.c -lcs50
   ```

4. **Run the Program**: Execute the compiled program by typing its name and providing the candidate names as command-line arguments.

   ```
   ./runoff Alice Bob Charlie
   ```

5. **Follow the Prompts**: The program will prompt you to enter the number of voters and then ask each voter to rank the candidates in order of preference.

6. **View Election Result**: The program will display the name of the winner of the election based on the ranked-choice voting system.

## Program Overview

The `runoff.c` program implements a runoff election simulation using a ranked-choice voting system. Here's an overview of the important components of the program:

- A two-dimensional array `preferences` is used to store the ranked preferences of each voter. The element `preferences[i][j]` stores the index of the candidate who is the jth preference for voter i.

- A `candidate` struct is defined, containing fields for the candidate's name, the number of votes they received, and a boolean indicating whether they are eliminated.

- An array of `candidate` structs named `candidates` is used to store the candidate information.

- The program tracks the total number of voters and candidates using the global variables `voter_count` and `candidate_count`.

- The program includes several functions: `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie`, and `eliminate`. These functions are responsible for various aspects of the runoff election simulation.

## Usage

Here's how you can use the program:

1. Provide candidate names as command-line arguments when running the program.

   ```
   ./runoff Alice Bob Charlie
   ```

2. Enter the number of voters when prompted.

3. For each voter, rank the candidates in order of preference.

4. After all preferences are recorded, the program will display the name of the winner based on the ranked-choice voting system.

   ```
   ./runoff Alice Bob Charlie
   Number of voters: 5
   Rank 1: Alice
   Rank 2: Charlie
   Rank 3: Bob

   Rank 1: Alice
   Rank 2: Charlie
   Rank 3: Bob

   Rank 1: Bob
   Rank 2: Charlie
   Rank 3: Alice

   Rank 1: Bob
   Rank 2: Charlie
   Rank 3: Alice

   Rank 1: Charlie
   Rank 2: Alice
   Rank 3: Bob

   Alice
   ```