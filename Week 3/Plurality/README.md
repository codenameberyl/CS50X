# Plurality

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 3 - Plurality Problem Set](https://cs50.harvard.edu/x/2023/psets/3/plurality/). The "Plurality" program simulates a plurality vote election, where candidates receive votes from voters, and the candidate with the highest number of votes wins the election.

## Getting Started

To get started with the program, follow these steps:

1. **Download the Source Code**: Download the source code for the program using the provided link and extract the contents of the ZIP file. You will find a file named `plurality.c`.

2. **Navigate to the Program Directory**: Open a terminal and navigate to the directory where the `plurality.c` file is located. You can do this by using the `cd` command.

   ```
   cd path/to/plurality-directory
   ```

3. **Compile the Program**: Compile the `plurality.c` file to create the executable program. Use the following command:

   ```
   clang -o plurality plurality.c -lcs50
   ```

4. **Run the Program**: Execute the compiled program by typing its name and providing the candidate names as command-line arguments.

   ```
   ./plurality Alice Bob Charlie
   ```

5. **Follow the Prompts**: The program will prompt you to enter the number of voters and then ask each voter to vote for a candidate.

6. **View Election Result**: The program will display the winner (or winners) of the election based on the plurality vote.

## Program Overview

The `plurality.c` program implements a simple plurality election simulation. Here's an overview of the important components of the program:

- A `candidate` struct is defined, containing fields for the candidate's name and the number of votes they have received.

- An array of `candidate` structs named `candidates` is used to store the candidate information.

- The `vote` function takes a voter's choice and checks if the choice matches any of the candidate names. If a match is found, the candidate's vote count is incremented, and the function returns `true`. If no match is found, it returns `false`.

- The `print_winner` function determines the candidate(s) with the highest number of votes and prints their names. If multiple candidates have the same maximum votes, all their names are printed.

## Usage

Here's how you can use the program:

1. Provide candidate names as command-line arguments when running the program.

   ```
   ./plurality Alice Bob Charlie
   ```

2. Enter the number of voters when prompted.

3. For each voter, enter the name of the chosen candidate.

4. After all votes are cast, the program will display the name(s) of the winner(s) based on the plurality vote.

   ```
   $ ./plurality Alice Bob
   Number of voters: 3
   Vote: Alice
   Vote: Bob
   Vote: Alice
   Alice
   ```

   ```
   $ ./plurality Alice Bob
   Number of voters: 3
   Vote: Alice
   Vote: Charlie
   Invalid vote.
   Vote: Alice
   Alice
   ```

   ```
   $ ./plurality Alice Bob Charlie
   Number of voters: 5
   Vote: Alice
   Vote: Charlie
   Vote: Bob
   Vote: Bob
   Vote: Alice
   Alice
   Bob
   ```

## Testing

Be sure to test your program to ensure it handles different scenarios correctly:

- Elections with different numbers of candidates (up to the maximum of 9).
- Voting for candidates by name.
- Invalid votes for candidates who are not on the ballot.
- Printing the winner of the election if there is only one.
- Printing the winners of the election if there are multiple candidates with the maximum votes.

## Conclusion

The "Plurality Election Simulation" program provides a basic understanding of how a plurality vote election works. By analyzing the provided code and completing the `vote` and `print_winner` functions, you can simulate an election and determine the winner(s) based on the votes cast by voters.

Feel free to customize and enhance this README to include any additional information or instructions that you think would be helpful.