#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int letters;
int words;
int sentences;

int main(void)
{
    // User prompt for input
    string text = get_string("Text: ");

    // Get text length
    int n = strlen(text);

    // add +1 if the text starts with alphanumeric letters
    if (isalnum(text[0]))
    {
        words = 1;
    }

    // count words
    for (int i = 0; i < n; i++)
    {
        // count letters
        if (isalnum(text[i]))
        {
            letters++;
        }

        // count words
        if (text[i] == 32 && text[i - 1] != 32)
        {
            words++;
        }

        // count sentences
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sentences++;
        }
    }

    // calculate Coleman-Liau index
    int grade = round(0.0588 * (100 * (float) letters / (float) words) - 0.296 * (100 * (float) sentences / words) - 15.8);

    // print result
    if (grade <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade < 16)
    {
        printf("Grade %i\n", grade);
    }
    else
    {
        printf("Grade 16+\n");
    }
}