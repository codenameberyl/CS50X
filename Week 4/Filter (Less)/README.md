# Filter (Less)

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 4 - Filter (Less) Problem Set](https://cs50.harvard.edu/x/2023/psets/4/filter/less/). This program applies various filters to BMP images, including grayscale, sepia, reflection, and blur filters.

## Usage

Compile the program using the provided Makefile:

```bash
make filter
```

Apply filters to images using the following command:

```bash
./filter -f FILTER_TYPE INPUT.bmp OUTPUT.bmp
```

- `FILTER_TYPE`: The type of filter to apply. Use `g` for grayscale, `s` for sepia, `r` for reflection, and `b` for blur.
- `INPUT.bmp`: The name of the input BMP image file.
- `OUTPUT.bmp`: The name of the output BMP image file after the filter is applied.

For example, to apply the grayscale filter to an image named `input.bmp` and generate an output image named `output.bmp`, use the following command:

```bash
./filter -g input.bmp output.bmp
```

## Filters

### Grayscale Filter

The grayscale filter converts an image to a black-and-white version of the original image. It does this by setting each pixel's red, green, and blue values to the average of their original values.

### Sepia Filter

The sepia filter gives images an old-timey feel by applying a reddish-brown tone to the image. It calculates new red, green, and blue values for each pixel based on the original color values using a specified formula.

### Reflection Filter

The reflection filter horizontally flips the image, creating a reflection effect as if the image were placed in front of a mirror.

### Blur Filter

The blur filter applies a box-blur effect to the image, softening the appearance of the image. It calculates the new color values for each pixel by averaging the color values of neighboring pixels within a 3x3 box.

## Implementation Details

- The program reads and writes BMP image files, extracting pixel data and manipulating color values.
- Functions are implemented to apply each filter to the image.
- Rounding is used to ensure that floating-point values are converted to integers for color values.

## Compilation and Execution

1. Compile the program using the provided Makefile:

```bash
make filter
```

2. Apply filters to images using the following command:

```bash
./filter -f FILTER_TYPE INPUT.bmp OUTPUT.bmp
```

## Examples

- Applying the grayscale filter:

```bash
./filter -g images/yard.bmp out.bmp
```

- Applying the sepia filter:

```bash
./filter -s images/yard.bmp out.bmp
```

- Applying the reflection filter:

```bash
./filter -r images/yard.bmp out.bmp
```

- Applying the blur filter:

```bash
./filter -b images/yard.bmp out.bmp
```