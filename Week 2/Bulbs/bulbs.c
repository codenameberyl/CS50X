#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // Get the message from the user
    string message = get_string("Message: ");

    // Iterate through each character in the message
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        char c = message[i];

        // Convert the character to its ASCII value
        int ascii_value = (int) c;

        // Convert the ASCII value to an 8-bit binary number
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            int bit = (ascii_value >> j) & 1; // Extract the j-th bit
            print_bulb(bit);
        }

        // Print a newline after each byte
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
