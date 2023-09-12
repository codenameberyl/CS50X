# Lab 1: Population Growth

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 1 - Lab 1: Population](https://cs50.harvard.edu/x/2023/labs/1/). This program calculates the number of years required for a population of llamas to grow from a start size to an end size, considering birth and death rates.

## Getting Started

To run this program, you need to have `cs50.h` and `stdio.h` libraries installed. You can compile and execute the program using the following commands:

```bash
make population
./population
```

## Program Overview

The program prompts the user for a starting population size and an ending population size. It then calculates the number of years required for the population to reach at least the size of the end value. Finally, the program prints the number of years required for the llama population to reach the end size.

## Implementation Details

The program uses loops and conditional statements to ensure valid input for the starting and ending population sizes. It calculates the number of years using a loop that updates the population size based on birth and death rates.

## Features

- Input validation for starting and ending population sizes.
- Calculation of years required for population growth.
- Proper handling of edge cases where start size equals end size.

## How to Use

1. Run the compiled program using `./population`.
2. Enter the starting population size when prompted.
3. Enter the ending population size when prompted.
4. The program will display the number of years required for the population to reach the end size.

## Example Usages

### Example 1

```bash
$ ./population
Start size: 1200
End size: 1300
Years: 1
```

### Example 2

```bash
$ ./population
Start size: -5
Start size: 3
Start size: 9
End size: 5
End size: 18
Years: 8
```

### Example 3

```bash
$ ./population
Start size: 20
End size: 1
End size: 10
End size: 100
Years: 20
```

### Example 4

```bash
$ ./population
Start size: 100
End size: 1000000
Years: 115
```

## Conclusion

The **Population Growth Calculator** is a useful tool to estimate the time required for a population to grow from a given start size to an end size. The program handles various scenarios, provides clear prompts, and delivers accurate results.