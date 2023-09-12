# Mario (More Comfortable)

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 1 - Mario (More) Problem Set](https://cs50.harvard.edu/x/2023/psets/1/mario/more/). This program, named `mario`, builds two adjacent pyramids using hashes (#) as bricks. The height of the pyramids is determined by user input, which should be a positive integer between 1 and 8, inclusive.

## Getting Started

To run this program, you need to have the `cs50.h` library installed. You can compile and execute the program using the following commands:

```bash
make mario
./mario
```

## Program Overview

The program prompts the user for the height of the pyramids, ensuring that the input is within the range of 1 to 8. It then uses nested loops to print the two adjacent pyramids with the specified height, leaving a gap of two spaces between them.

## Features

- Prompting the user for the pyramids' height.
- Building two adjacent pyramids using spaces and hashes, with a gap in between.

## How to Use

1. Run the compiled program using `./mario`.
2. Enter the height of the pyramids when prompted.
3. The program will display the two adjacent pyramids with the specified height and a gap in between.

## Example Usage

```bash
$ ./mario
Height: 5
       #  #
      ##  ##
     ###  ###
    ####  ####
   #####  #####
```

```bash
$ ./mario
Height: 3
   #  #
  ##  ##
 ###  ###
```

## Implementation Details

The program uses nested loops to print the appropriate number of spaces and hashes to create the two adjacent pyramids. The gap between the pyramids is two spaces.

## Conclusion

The **Mario (More Comfortable) Pyramid Builder** program builds two adjacent pyramids using basic programming constructs such as loops and conditional statements. It introduces the concept of nested loops and provides practice in user input validation.