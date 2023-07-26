// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1170;
int word_count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hashed_word = hash(word);
    node *cursor = table[hashed_word];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Hash function that is sorted by first letter + length of word
    int first_letter = (toupper(word[0]) - 'A') * LENGTH;
    int hash_number = first_letter + strlen(word);
    return hash_number;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    // Create an array to store words from dictionary
    char word_storage[LENGTH + 1];
    while (fscanf(dict, "%s", word_storage) != EOF)
    {
        node *node_temp = malloc(sizeof(node));
        if (node_temp == NULL)
        {
            return false;
        }
        strcpy(node_temp->word, word_storage);
        int hash_number = hash(word_storage);

        if (table[hash_number] == NULL)
        {
            node_temp->next = NULL;
        }
        else
        {
            node_temp->next = table[hash_number];
        }
        table[hash_number] = node_temp;
        word_count += 1;
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

void node_recursion(node *tmp)
{
    if (tmp->next != NULL)
    {
        node_recursion(tmp->next);
    }
    free(tmp);
}
// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            node_recursion(table[i]);
        }
    }
    return true;
}
