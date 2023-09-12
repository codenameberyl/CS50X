# Mario (Less Comfortable)

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 1 - Mario (Less) Problem Set](https://cs50.harvard.edu/x/2023/psets/1/mario/less/). This program, named `mario`, builds a right-aligned pyramid using hashes (#) as bricks. The height of the pyramid is determined by user input, which should be a positive integer between 1 and 8, inclusive.

## Getting Started

To run this program, you need to have the `cs50.h` library installed. You can compile and execute the program using the following commands:

```bash
make mario
./mario
```

## Program Overview

The program prompts the user for the height of the pyramid, ensuring that the input is within the range of 1 to 8. It then uses nested loops to print the right-aligned pyramid with the specified height using spaces and hashes.

## Features

- Prompting the user for the pyramid's height.
- Building a right-aligned pyramid using spaces and hashes.

## How to Use

1. Run the compiled program using `./mario`.
2. Enter the height of the pyramid when prompted.
3. The program will display the right-aligned pyramid with the specified height.

## Example Usage

```bash
$ ./mario
Height: 5
    #
   ##
  ###
 ####
#####
```

```bash
$ ./mario
Height: 3
  #
 ##
###
```

## Implementation Details

The program uses a loop to prompt the user for the pyramid's height, ensuring the input is valid. It then utilizes nested loops to print the appropriate number of spaces and hashes to create the right-aligned pyramid.

## Conclusion

The **Mario (Less Comfortable)** program is a fun exercise in using loops to create visual patterns. It introduces the concept of nested loops and user input validation, providing a hands-on experience with basic programming constructs.