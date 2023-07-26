#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    int number_of_years = 0;

    while (start_size < end_size)
    {
        start_size = start_size + (start_size / 3) - (start_size / 4);
        number_of_years++;
    }

    printf("Years: %i\n", number_of_years);
}
