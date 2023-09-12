#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s input.wav output.wav\n", argv[0]);
        return 1;
    }

    // Open input file for reading
    FILE *input_file = fopen(argv[1], "rb");
    if (input_file == NULL)
    {
        fprintf(stderr, "Could not open %s for reading.\n", argv[1]);
        return 1;
    }

    // Read header
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input_file);

    // Use check_format to ensure WAV format
    if (!check_format(header))
    {
        fprintf(stderr, "Input is not a WAV file.\n");
        fclose(input_file);
        return 1;
    }

    // Open output file for writing
    FILE *output_file = fopen(argv[2], "wb");
    if (output_file == NULL)
    {
        fprintf(stderr, "Could not open %s for writing.\n", argv[2]);
        fclose(input_file);
        return 1;
    }

    // Write header to file
    fwrite(&header, sizeof(WAVHEADER), 1, output_file);

    // Use get_block_size to calculate size of block
    int block_size = get_block_size(header);

    // Calculate number of blocks in the audio
    int num_blocks = header.subchunk2Size / block_size;

    // Read and Write reversed audio to file
    for (int i = num_blocks - 1; i >= 0; i--)
    {
        BYTE *block = (BYTE *) malloc(block_size);
        fseek(input_file, sizeof(WAVHEADER) + i * block_size, SEEK_SET);
        fread(block, sizeof(BYTE), block_size, input_file);
        fwrite(block, sizeof(BYTE), block_size, output_file);
        free(block);
    }

    // Close files
    fclose(input_file);
    fclose(output_file);

    return 0;
}

int check_format(WAVHEADER header)
{
    return header.chunkID[0] == 'R' && header.chunkID[1] == 'I' && header.chunkID[2] == 'F' && header.chunkID[3] == 'F' &&
           header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E';
}

int get_block_size(WAVHEADER header)
{
    return header.numChannels * header.bitsPerSample / 8;
}