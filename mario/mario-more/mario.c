// Creates a pyramid of blocks for mario game design

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Asks the user for height of blocks
    int blocks;
    do
    {
        blocks = get_int("How many blocks high?  ");
    }
    while (blocks < 1 || blocks > 8);

    // Main Loop that runs the code inside the amount of blocks the user input (height)
    int c;
    for (c = 0; c < blocks; c++)
    {
        int i;
        int j;
        int s;

        // Loop that prints the initial spacing before a first block on a line
        for (s = c; s < (blocks - 1) ; s++)
        {
            printf(" ");
        }

        // Prints the first set of blocks on a line
        for (i = 0; i <= c; i++)
        {
            printf("#");
        }

        // Prints a gap between our 2 sets of blocks
        printf("  ");

        // Prints the second set of blocks on a line
        for (j = 0; j <= c; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}