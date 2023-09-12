#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char c, int key);

int main(int argc, string argv[])
{
    // Check if there is exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if the argument contains only digits
    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Convert the argument to an integer
    int key = atoi(argv[1]);

    // Get plaintext input from the user
    string plaintext = get_string("plaintext: ");

    // Print "ciphertext: "
    printf("ciphertext: ");

    // Iterate through each character in the plaintext
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        // Rotate alphabetical characters by key positions
        char encrypted = rotate(c, key);

        // Print the rotated character
        printf("%c", encrypted);
    }

    // Print a new line
    printf("\n");

    return 0;
}

bool only_digits(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int key)
{
    if (isalpha(c))
    {
        char base = isupper(c) ? 'A' : 'a';
        return (c - base + key) % 26 + base;
    }
    return c;
}