#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    // Loop over the matrix
    for (int row = 0; row < width; row++)
    {
        for (int col = 0; col < height; col++)
        {
            // Change the color of any black pixel to new color
            if (image[col][row].rgbtBlue == 0 &&
                image[col][row].rgbtGreen == 0 &&
                image[col][row].rgbtRed == 0)
            {
                image[col][row].rgbtBlue = 69;
                image[col][row].rgbtGreen = 101;
                image[col][row].rgbtRed = 178;
            }
        }
    }
}
