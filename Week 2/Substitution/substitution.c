#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool is_valid_key(string key);
string encrypt(string plaintext, string key);

int main(int argc, string argv[])
{
    // Check if there is exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Get the key from the command-line argument
    string key = argv[1];

    // Check if the key is valid
    if (!is_valid_key(key))
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Get plaintext input from the user
    string plaintext = get_string("plaintext: ");

    // Encrypt the plaintext and print the result
    string ciphertext = encrypt(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

bool is_valid_key(string key)
{
    // Check if the key has exactly 26 characters
    if (strlen(key) != 26)
    {
        return false;
    }

    // Create an array to keep track of characters
    bool found[26] = {false};

    // Iterate through each character in the key
    for (int i = 0, n = strlen(key); i < n; i++)
    {
        // Check if the character is alphabetic
        if (!isalpha(key[i]))
        {
            return false;
        }

        // Convert the character to uppercase
        char c = toupper(key[i]);

        // Check if the character has been seen before
        if (found[c - 'A'])
        {
            return false;
        }

        // Mark the character as seen
        found[c - 'A'] = true;
    }

    return true;
}

string encrypt(string plaintext, string key)
{
    // Create a mapping of the alphabet to the key
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string ciphertext = plaintext;

    // Iterate through each character in the plaintext
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        // Determine whether the character is uppercase or lowercase
        if (isupper(c))
        {
            ciphertext[i] = toupper(key[c - 'A']);
        }
        else if (islower(c))
        {
            ciphertext[i] = tolower(key[c - 'a']);
        }
        else
        {
            // Non-alphabetical characters are not encrypted
            ciphertext[i] = c;
        }
    }

    return ciphertext;
}