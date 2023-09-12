#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    for (int i = 0; i < n; i++)
    {
        for (int k = (n - i); k > 1; k--)
        {
            printf(" ");
        }
        for (int j = -1; j < i; j++)
        {
            printf("#");
        }
        // Print 2 spaces here
        printf("  ");
        for (int l = -1; l < i; l++)
        {
            printf("#");
        }
        printf("\n");
    }
}