# Lab 4: Volume

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 4 - Lab 4: Volume](https://cs50.harvard.edu/x/2023/labs/4/volume/). This program is designed to modify the volume of an audio file in the WAV format. It reads an input audio file, scales the volume by a specified factor, and then writes the modified audio data to an output audio file.

## Usage

The program accepts the following command-line arguments:

```
./volume INPUT.wav OUTPUT.wav FACTOR
```

- `INPUT.wav`: The name of the original audio file.
- `OUTPUT.wav`: The name of the new audio file with modified volume.
- `FACTOR`: The amount by which the volume of the original audio file should be scaled.

For example, running the program with `./volume input.wav output.wav 2.0` will double the volume of the audio in `input.wav` and save the modified audio in `output.wav`.

## Implementation Details

1. The program opens the input and output audio files and determines the scaling factor provided in the command-line arguments.
2. It reads the header of the input file (44 bytes) and copies it to the output file.
3. The program then reads the audio samples from the input file one at a time, modifies their values by multiplying them with the specified factor, and writes the modified samples to the output file.
4. The program closes the input and output files after processing.

## Compilation and Execution

Compile the program using the following command:

```bash
gcc -o volume volume.c
```

Execute the program with appropriate command-line arguments:

```bash
$ ./volume input.wav output.wav 2.0
```

```bash
$ ./volume input.wav output.wav 1.0
```

```bash
$ ./volume input.wav output.wav 0.5
```