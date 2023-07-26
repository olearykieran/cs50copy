#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < width; row++)
    {
        for (int col = 0; col < height; col++)
        {
            int average = round((image[col][row].rgbtBlue + image[col][row].rgbtGreen + image[col][row].rgbtRed) / 3.0);
            image[col][row].rgbtBlue = average;
            image[col][row].rgbtGreen = average;
            image[col][row].rgbtRed = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < width; row++)
    {
        for (int col = 0; col < height; col++)
        {
            int sblue = round(.272 * image[col][row].rgbtRed + .534 * image[col][row].rgbtGreen + .131 * image[col][row].rgbtBlue);
            int sgreen = round(.349 * image[col][row].rgbtRed + .686 * image[col][row].rgbtGreen + .168 * image[col][row].rgbtBlue);
            int sred = round(.393 * image[col][row].rgbtRed + .769 * image[col][row].rgbtGreen + .189 * image[col][row].rgbtBlue);

            image[col][row].rgbtBlue = fmin(255, sblue);

            image[col][row].rgbtGreen = fmin(255, sgreen);

            image[col][row].rgbtRed = fmin(255, sred);

        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE storage;

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width / 2; col++)
        {
            storage = image[row][col];
            image[row][col] = image[row][width - col - 1];
            image[row][width - col - 1] = storage;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Store a temporary value
    RGBTRIPLE storage[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            storage[row][col] = image[row][col];

        }
    }

    // New loop to work on individual pixels as well as the surrounding pixels
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            //
            int red = 0;
            int blue = 0;
            int green = 0;
            int sum = 0;
            for (int i = -1; i < 2; i++)
            {
                for (int j = -1; j < 2; j++)
                {
                    // Set boundaries and limits
                    if ((row + i >= 0 && row + i < height) && (col + j >= 0 && col + j < width))
                    {
                        sum++;
                        red += storage[row + i][col + j].rgbtRed;
                        green +=  storage[row + i][col + j].rgbtGreen;
                        blue +=  storage[row + i][col + j].rgbtBlue;
                    }
                }
            }
            // Update original pixel with average of 9 surrounding pixels
            image[row][col].rgbtRed = round(red / (float) sum);
            image[row][col].rgbtGreen = round(green / (float)  sum);
            image[row][col].rgbtBlue = round(blue / (float) sum);
        }
    }
}
