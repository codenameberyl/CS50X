#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for correct command-line usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s IMAGE\n", argv[0]);
        return 1;
    }

    // Open the forensic image file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s for reading.\n", argv[1]);
        return 1;
    }

    BYTE buffer[512];    // Buffer to store 512 bytes of data
    int image_count = 0; // Counter for naming the output images
    FILE *img = NULL;    // File pointer for the output image

    // Iterate through the file
    while (fread(buffer, sizeof(BYTE), 512, file) == 512)
    {
        // Check for the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the previous image file if open
            if (img != NULL)
            {
                fclose(img);
            }

            // Create a new JPEG image file
            char filename[8];
            sprintf(filename, "%03i.jpg", image_count);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                fclose(file);
                fprintf(stderr, "Could not create %s for writing.\n", filename);
                return 1;
            }

            image_count++;
        }

        // Write data to the output image file
        if (img != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, img);
        }
    }

    // Close any open files
    fclose(file);
    if (img != NULL)
    {
        fclose(img);
    }

    return 0;
}