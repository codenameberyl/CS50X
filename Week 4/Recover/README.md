# Recover

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 4 - Recover Problem Set](https://cs50.harvard.edu/x/2023/psets/4/recover/). This program, called "recover," is designed to recover JPEG images from a forensic image file. When files are deleted or erased, they are not always immediately removed from storage devices. This program capitalizes on the structure of JPEG files to identify and recover them from a provided forensic image.

## Requirements

- A computer with a compatible C compiler.
- A forensic image file (e.g., "card.raw") from which the JPEGs need to be recovered.

## How to Use

1. Compile the program: Open a terminal and navigate to the directory containing the "recover.c" file. Compile the program using the following command:

   ```
   gcc -o recover recover.c
   ```

2. Run the program: Execute the compiled program with the name of the forensic image file as a command-line argument. For example:

   ```
   ./recover card.raw
   ```

3. Output: The program will read the forensic image file, identify and recover JPEG images, and store them in the current working directory. The recovered images will be named as "001.jpg," "002.jpg," and so on.

## Program Explanation

The program follows these steps to recover JPEG images:

1. Check Command-Line Usage: The program checks if the correct command-line argument is provided. If not, it displays the correct usage and returns 1.

2. Open the Forensic Image: The program attempts to open the forensic image file provided as a command-line argument. If the file cannot be opened, an error message is displayed, and the program returns 1.

3. Read and Process Data: The program reads data from the forensic image in 512-byte blocks and processes them to identify JPEG image signatures.

4. Detect JPEG Signature: The program checks if the current 512-byte block contains the JPEG signature. If found, a new JPEG image file is created and opened for writing.

5. Write Data: As long as a JPEG image file is open, the program continues to write the data blocks to the file.

6. Close Files: The program closes all open files before exiting.

## Conclusion

The "recover" program is a valuable tool for recovering JPEG images from a forensic image. It uses the distinctive signature of JPEG files to identify and recover them, allowing users to restore deleted images from storage devices.

**Note:** Before running the program on important files, make sure to back up your data, as data recovery can be a delicate process.

Feel free to experiment with the program and understand how it works to gain a deeper understanding of file recovery and file formats.