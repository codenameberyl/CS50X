# Filter (More)

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 4 - Filter (More) Problem Set](https://cs50.harvard.edu/x/2023/psets/4/filter/more/). This is a C program that applies different filters to BMP images. The program supports the following filters: grayscale, reflection, blur, and edge detection. The program uses the BMP file format, where each pixel in the image is represented by its red, green, and blue color values.

## Compilation

To compile the program, use the provided Makefile by executing the following command in your terminal:

```bash
make filter
```

## Usage

Once the program is compiled, you can apply filters to images using the following command-line syntax:

```bash
./filter -<filter> INFILE.bmp OUTFILE.bmp
```

Replace `<filter>` with the desired filter: `g` for grayscale, `r` for reflection, `b` for blur, and `e` for edge detection. Replace `INFILE.bmp` with the input image's filename and `OUTFILE.bmp` with the desired output image's filename.

## Filters

### Grayscale Filter

To convert an image to grayscale, use the `-g` flag. The grayscale filter calculates the average of the red, green, and blue color values for each pixel and sets all three values to the calculated average, resulting in a black-and-white version of the image.

Example usage:
```bash
./filter -g input.bmp grayscale_output.bmp
```

### Reflection Filter

To reflect an image horizontally, use the `-r` flag. The reflection filter swaps the pixels on the left half of the image with the corresponding pixels on the right half of the image.

Example usage:
```bash
./filter -r input.bmp reflected_output.bmp
```

### Blur Filter

To apply a blur effect to an image, use the `-b` flag. The blur filter replaces each pixel's color values with the average color values of its surrounding pixels, creating a softened appearance.

Example usage:
```bash
./filter -b input.bmp blurred_output.bmp
```

### Edge Detection Filter

To detect edges in an image, use the `-e` flag. The edge detection filter uses the Sobel operator to calculate the gradient magnitude of each pixel, highlighting the edges between objects in the image.

Example usage:
```bash
./filter -e input.bmp edges_output.bmp
```