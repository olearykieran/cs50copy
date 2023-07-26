#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
void answer(int count);

int main(void)
{
    // Ask user for text
    string text = get_string("Text: ");
    // Gets letter count
    int letters = count_letters(text);
    // Gets word count
    float words = count_words(text);
    // Gets sentence count
    int sentences = count_sentences(text);
    // Runs Input throught the Coleman-Liau index formula
    float L = letters / words * 100;
    float S = sentences / words * 100;
    float formula = 0.0588 * L - 0.296 * S - 15.8;
    float rounded = round(formula);
    // Prints grade level
    answer(rounded);
}

// Gets letter count
int count_letters(string text)
{
    int letter_total = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letter_total++;
        }
    }
    return letter_total;
}

// Gets word count
int count_words(string text)
{
    int word_total = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            word_total++;
        }
    }
    return word_total + 1;
}

// Gets sentence count
int count_sentences(string text)
{
    int sentence_total = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        char c = text[i];
        switch (c)
        {
            case '.':
                sentence_total++;
                break;

            case '?':
                sentence_total++;
                break;

            case '!':
                sentence_total++;
                break;

            default:
                break;
        }
    }
    return sentence_total;
}

// Prints grade level
void answer(int count)
{
    int grade = 0;
    if (count <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (count >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", count);
    }
}