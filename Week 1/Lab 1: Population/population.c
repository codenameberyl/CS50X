#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start;
    int end;

    // Prompt for start size
    do
    {
        start = get_int("Start Size? ");
    }
    while (start < 9);

    // Prompt for end size
    do
    {
        end = get_int("Start Size? ");
    }
    while (end < start);

    // Calculate number of years until we reach threshold
    int years = 0;

    if (start == end)
    {
        years = 0;
    }
    else
    {
        do
        {
            start = start + (start / 3) - (start / 4);
            years++;
        }
        while (start < end);
    }

    // Print number of years
    printf("Years: %i\n", years);
}
