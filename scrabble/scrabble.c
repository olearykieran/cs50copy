#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");

    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Compare scores and return results
    if (score1 > score2)
    {
        printf("Player 1 wins\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

// Adds up the score of each word that was inputted by iterating over each character in the string
int compute_score(string word)
{
    int w_score = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        if (isalpha(word[i]))
            // Matches up the word array with the points array by using the difference from the ASCII table
        {
            int match_up_letter_with_array = toupper(word[i]) - 'A';
            w_score += POINTS[match_up_letter_with_array];
        }
    }
    return w_score;
}
