# Tideman

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 3 - Tideman Problem Set](https://cs50.harvard.edu/x/2023/psets/3/tideman/). This program implements the Tideman election method, also known as "ranked pairs." The Tideman method is a ranked-choice voting system that aims to find the Condorcet winner of an election if one exists. The Condorcet winner is the candidate who would win in a head-to-head matchup against any other candidate.

## Background

In traditional plurality voting, the candidate with the most votes wins. However, this method may lead to suboptimal outcomes, especially when there are more than two candidates. Ranked-choice voting systems, like Tideman, allow voters to rank candidates in order of preference. The Tideman algorithm constructs a graph of candidates, where arrows represent preferences between candidates. The winner is the candidate with no arrows pointing towards them, ensuring that they are preferred over all other candidates in head-to-head matchups.

## Program Components

### `tideman.c`

This is the main C program that simulates the Tideman election. It includes the following functions:

1. `bool vote(int rank, string name, int ranks[])`: Records a voter's preference for a candidate at a specific rank.
2. `void record_preferences(int ranks[])`: Records the preferences of a voter based on their ranks.
3. `void add_pairs(void)`: Adds pairs of candidates where one is preferred over the other.
4. `void sort_pairs(void)`: Sorts the pairs of candidates in decreasing order of strength of victory.
5. `bool forms_cycle(int source, int destination)`: Checks if adding an edge from the source candidate to the destination candidate creates a cycle in the graph.
6. `void lock_pairs(void)`: Locks pairs into the candidate graph without creating cycles.
7. `void print_winner(void)`: Prints the name of the election winner.

### Compilation and Execution

To compile and execute the program, use the following commands:

```
gcc -o tideman tideman.c -lcs50
./tideman [candidate ...]
```

Replace `[candidate ...]` with the list of candidate names (up to a maximum of 9 candidates).

## Usage

1. Run the program using the above compilation and execution commands.
2. Enter the number of voters when prompted.
3. For each voter, provide the ranking of candidates. The ranking is done by specifying the candidate names in order of preference (1st preference, 2nd preference, etc.).
4. After all votes are collected, the program will determine the winner of the election using the Tideman method and display the winner's name.

   ```
   ./tideman Alice Bob Charlie
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

   Charlie
   ```