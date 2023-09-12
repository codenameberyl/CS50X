#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round(((float) image[i][j].rgbtRed + (float) image[i][j].rgbtGreen + (float) image[i][j].rgbtBlue) / 3);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels horizontally
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    // Create a copy of the image to store the blurred version
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    // Apply blur to each pixel in the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;
            int totalRed = 0;
            int totalGreen = 0;
            int totalBlue = 0;

            // Iterate over the surrounding pixels in a 3x3 box
            for (int row = i - 1; row <= i + 1; row++)
            {
                for (int col = j - 1; col <= j + 1; col++)
                {
                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        count++;
                        totalRed += temp[row][col].rgbtRed;
                        totalGreen += temp[row][col].rgbtGreen;
                        totalBlue += temp[row][col].rgbtBlue;
                    }
                }
            }

            // Update the pixel with the average color values
            image[i][j].rgbtRed = round((float) totalRed / count);
            image[i][j].rgbtGreen = round((float) totalGreen / count);
            image[i][j].rgbtBlue = round((float) totalBlue / count);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Sobel kernels for edge detection
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    RGBTRIPLE temp[height][width];

    // Create a copy of the image to store the edges version
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    // Apply edge detection to each pixel in the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int GxRed = 0, GxGreen = 0, GxBlue = 0;
            int GyRed = 0, GyGreen = 0, GyBlue = 0;

            // Iterate over the surrounding pixels in a 3x3 box
            for (int row = i - 1; row <= i + 1; row++)
            {
                for (int col = j - 1; col <= j + 1; col++)
                {
                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        int weightX = Gx[row - i + 1][col - j + 1];
                        int weightY = Gy[row - i + 1][col - j + 1];

                        GxRed += weightX * temp[row][col].rgbtRed;
                        GxGreen += weightX * temp[row][col].rgbtGreen;
                        GxBlue += weightX * temp[row][col].rgbtBlue;

                        GyRed += weightY * temp[row][col].rgbtRed;
                        GyGreen += weightY * temp[row][col].rgbtGreen;
                        GyBlue += weightY * temp[row][col].rgbtBlue;
                    }
                }
            }

            // Calculate the final edge value for each color channel
            int edgeRed = round(sqrt(GxRed * GxRed + GyRed * GyRed));
            int edgeGreen = round(sqrt(GxGreen * GxGreen + GyGreen * GyGreen));
            int edgeBlue = round(sqrt(GxBlue * GxBlue + GyBlue * GyBlue));

            // Cap values at 255
            image[i][j].rgbtRed = (edgeRed > 255) ? 255 : edgeRed;
            image[i][j].rgbtGreen = (edgeGreen > 255) ? 255 : edgeGreen;
            image[i][j].rgbtBlue = (edgeBlue > 255) ? 255 : edgeBlue;
        }
    }
    return;
}
