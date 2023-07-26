#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Converts card number to a string so we can find the length
int length(long card_num);

// Formula for getting the sum of every other digit from the 2nd to last number of the credit card
int sum_of_alternate_digits(long card_num);

// Doubles the last digit and adds the digits together (not the integer)
int doubled_and_sum(long last_digit);

// Checks if the card number has the qualities of an amex card
bool isValidAmex(long card_num, int num_length);

// Checks if the card number has the qualities of a Master card
bool isValidMaster(long card_num, int num_length);

// Checks if the card number has the qualities of a visa card
bool isValidVisa(long card_num, int num_length);

int main(void)
{
    long cc_number;
    // Ask user for CC number
    do
    {
        cc_number = get_long("What is your Credit Card number? ");
    }
    while (cc_number < 0);

    // Assigning variables for functions
    int dig_length = length(cc_number);
    bool amex = isValidAmex(cc_number, dig_length);
    bool master = isValidMaster(cc_number, dig_length);
    bool visa = isValidVisa(cc_number, dig_length);
    int sum_every_other_digit = sum_of_alternate_digits(cc_number);

    // Runs the CC number through several functions to verify type and validity
    if (sum_every_other_digit % 10 != 0)
    {
        printf("INVALID\n");
    }
    else if (amex == true)
    {
        printf("AMEX\n");
    }
    else if (master == true)
    {
        printf("MASTERCARD\n");
    }
    else if (visa == true)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }

    // print tests to make sure numbers were valid
    // printf("%i", sum_every_other_digit);
    // printf("\n");
    // printf("%d", length(cc_number));
    // printf("\n");
}









// Formula for getting the sum of every other digit from the 2nd to last number of the credit card
int sum_of_alternate_digits(long card_num)
{
    int sum = 0;
    bool isOtherDigit = false;
    while (card_num > 0)
    {
        if (isOtherDigit == true)
        {
            int final_digit = card_num % 10;
            int product = doubled_and_sum(final_digit);
            sum = sum + product;
        }
        else
        {
            int final_digit = card_num % 10;
            sum = sum + final_digit;
        }
        isOtherDigit = !isOtherDigit;
        card_num = card_num / 10;
    }
    return sum;

}

// Doubles the last digit and adds the digits together (not the integer)
int doubled_and_sum(long last_digit)
{
    int sum = 0;
    int doubled = last_digit * 2;
    while (doubled > 0)
    {
        int last_digit_after_doubled = doubled % 10;
        sum = sum + last_digit_after_doubled;
        doubled = doubled / 10;
    }
    return sum;

}

// Converts card number to a string so we can find the length
int length(long card_num)
{
    char str[20];
    int len;
    len = snprintf(str, 20, "%ld", card_num);
    len = strlen(str);
    return len;
}

// Checks if the card number has the qualities of an amex card
bool isValidAmex(long card_num, int num_length)
{
    int first_two_dig = (card_num / 10000000000000);
    if ((num_length == 15) && (first_two_dig == 34 || first_two_dig == 37))
    {
        return true;
    }
    else
    {
        return false;
    }
}

// Checks if the card number has the qualities of a Master card
bool isValidMaster(long card_num, int num_length)
{
    int first_two_dig = (card_num / 100000000000000);
    if ((num_length == 16) && (first_two_dig > 50 && first_two_dig < 56))
    {
        return true;
    }
    else
    {
        return false;
    }
}

// Checks if the card number has the qualities of a visa card
bool isValidVisa(long card_num, int num_length)
{
    int first_dig_a = (card_num / 1000000000000000);
    int first_dig_b = (card_num / 1000000000000);
    if ((num_length == 13 || num_length == 16) && (first_dig_a == 4 || first_dig_b == 4))
    {
        return true;
    }
    else
    {
        return false;
    }
}