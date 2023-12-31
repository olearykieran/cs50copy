// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool lower = false;
    bool upper = false;
    bool num = false;
    bool symbol = false;
    for (int i = 0; i < strlen(password); i++)
    {
        if (islower(password[i]))
        {
            lower = true;
        }
        if (isupper(password[i]))
        {
            upper = true;
        }
        if (isdigit(password[i]))
        {
            num = true;
        }
        if (!isalnum(password[i]))
        {
            symbol = true;
        }
    }
    if (lower == true && upper == true && num == true && symbol == true)
    {
        return true;
    }
    return false;

}
