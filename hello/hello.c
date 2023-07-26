// Says hello to user

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get user name
    string i = get_string("What is your name?  ");

    // Prints output to user
    printf("hello, %s\n", i);
}