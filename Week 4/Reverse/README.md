# Reverse

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 4 - Reverse Problem Set](https://cs50.harvard.edu/x/2023/psets/4/reverse/). This program, named "reverse," is designed to reverse the audio data in a WAV file. It takes an input WAV file, processes it, and creates an output WAV file with the reversed audio. The program leverages the uncompressed nature of WAV files to manipulate the audio data easily.

## Requirements

- A computer with a compatible C compiler.
- An input WAV file that you want to reverse.

## How to Use

1. Compile the program: Open a terminal and navigate to the directory containing the "reverse.c" file. Compile the program using the following command:

   ```
   gcc -o reverse reverse.c
   ```

2. Run the program: Execute the compiled program with the name of the input WAV file and the desired output WAV file as command-line arguments. For example:

   ```
   ./reverse input.wav output.wav
   ```

3. Output: The program will read the input WAV file, reverse the audio data, and save it in the output WAV file. The output file will contain the same audio as the input, but played in reverse.

## Program Explanation

The program follows these steps to reverse the audio in a WAV file:

1. Check Command-Line Usage: The program checks if the correct command-line arguments are provided. If not, it displays the correct usage and returns 1.

2. Open Input File: The program attempts to open the input WAV file provided as a command-line argument in read-binary mode. If the file cannot be opened, an error message is displayed, and the program returns 1.

3. Read Header: The program reads the header of the input WAV file using the provided WAVHEADER struct.

4. Verify WAV Format: The program uses the `check_format` function to ensure that the input file is in the WAV format. If the format is not verified, an error message is displayed, and the program returns 1.

5. Open Output File: The program attempts to open the output WAV file provided as a command-line argument in write-binary mode. If the file cannot be opened, an error message is displayed, and the program returns 1.

6. Write Header: The program writes the header to the output file to maintain the same file structure as the input file.

7. Calculate Block Size: The program uses the `get_block_size` function to calculate the size of each audio block in bytes.

8. Reverse Audio: The program iterates through the audio blocks of the input file in reverse order. For each block, it reads the data, reverses it, and writes it to the output file.

9. Close Files: The program closes both the input and output files.

The "reverse" program provides a way to reverse the audio data in a WAV file. By leveraging the uncompressed nature of WAV files, the program can read, manipulate, and write the audio data in reverse order. This tool can be useful for various audio-related tasks and explorations.

**Note:** Make sure to have a backup of your original audio file before using this program, as it modifies the data.

Feel free to experiment with the program and analyze the results to gain insights into audio manipulation and file formats.