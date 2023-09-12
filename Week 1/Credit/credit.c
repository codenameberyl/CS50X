#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long card_num = 0;
    do
    {
        card_num = get_long("Number: ");
    }
    while (card_num < 1 || card_num > 9999999999999999);
    // Make a copy of the card number to be used and modified throughout the process.

    long long temp_num = card_num;

    // Isolate every digit from the credit card num ber using a loop and the variable 'digit'.
    // Keep track of the amount and position of each digit using variable 'count'.

    int count = 0;

    while (temp_num > 0)
    {
        temp_num = temp_num / 10;
        count++;
    }

    // Apply Luhn's algorithm.

    int sum = 0;

    temp_num = card_num;

    for (int i = 1; i <= count; i++)
    {
        int digit = temp_num % 10;

        if (i % 2 == 0)
        {
            digit *= 2;

            if (digit > 9)
            {
                digit -= 9;
            }
        }

        sum += digit;

        temp_num /= 10;
    }

    // Checking the validity of the number according to Luhn's algorithm

    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // If the number entered doesn't have the right amount of digits according
    // to variable 'count', declare the number as invalid.

    if (count != 13 && count != 15 && count != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    // Reset value of variable 'temp_num' and apply calculations that will isolate the first two digits.
    // Store the results in a variable 'company_id'.

    temp_num = card_num;

    while (temp_num > 100)
    {
        temp_num = temp_num / 10;
    }

    int company_id = temp_num;

    // Print the type of credit card depending on the company ID and amount of digits.

    if (company_id > 50 && company_id < 56 && count == 16)
    {
        printf("MASTERCARD\n");
    }
    else if ((company_id == 34 || company_id == 37) && (count == 15))
    {
        printf("AMEX\n");
    }
    else if ((company_id / 10 == 4) && (count == 13 || count == 16))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}