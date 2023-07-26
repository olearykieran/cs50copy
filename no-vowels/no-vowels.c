// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string replace(string word);

int main(int argc, string argv[])
{
    while (argc < 2 || argc > 2)
    {
        printf("ERROR ERROR ERROR\n");
        return 1;
    }
    printf("%s\n", replace(argv[1]));
}

string replace(string input)
{
    string output = input;
    for (int i = 0; i < strlen(input); i++)
    {
        char c = tolower(input[i]);
        switch (c)
        {
            case 'a':
                output[i] = '6';
                break;

            case 'e':
                output[i] = '3';
                break;

            case 'i':
                output[i] = '1';
                break;

            case 'o':
                output[i] = '0';
                break;

            default:
                break;
        }
    }
    return output;
}

// Your program must contain a function called replace which takes a string input and returns a string output.
// This function will change the following vowels to numbers: a becomes 6, e becomes 3, i becomes 1, o becomes 0 and u does not change.
// The input parameter for the replace function will be argv[1] and the return value is the converted word.
// The main function will then print the converted word, followed by \n.
// You may want to try using the switch statement in your replace function.