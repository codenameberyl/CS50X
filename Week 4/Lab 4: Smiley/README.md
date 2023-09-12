# Lab 4: Smiley

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 4 - Lab 4: Smiley](https://cs50.harvard.edu/x/2023/labs/4/smiley/). This program is designed to colorize an image by changing all the black pixels to a color of your choosing. It works with images in the BMP format, where each pixel is represented by an RGB triplet consisting of red, green, and blue color components.

## Usage

Compile the program using the provided Makefile:

```bash
make colorize
```

Execute the program with the following command:

```bash
./colorize INPUT.bmp OUTPUT.bmp
```

- `INPUT.bmp`: The name of the original BMP image file.
- `OUTPUT.bmp`: The name of the new BMP image file with colorized pixels.

For example, running the program with `./colorize smiley.bmp smiley_out.bmp` will create a new BMP image file named `smiley_out.bmp` where all the black pixels in the original `smiley.bmp` image are changed to a color of your choice.

## Implementation Details

The `colorize` function provided in the `helpers.c` file iterates through each pixel in the image and changes the color of black pixels to a specified color. In this implementation, black pixels are changed to a red color.

## Compilation and Execution

1. Compile the program using the provided Makefile:

```bash
make colorize
```

2. Execute the program with the appropriate command-line arguments:

```bash
./colorize smiley.bmp smiley_out.bmp
```