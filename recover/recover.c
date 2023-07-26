#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512

typedef uint8_t BYTE;

/* typedef struct
{
    BYTE first
    BYTE second
    BYTE third
    BYTE fourth
}
JPEG */

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open files and return notification if it fails
    FILE *memory_card = fopen(argv[1], "r");
    if (memory_card == NULL)
    {
        printf("Could not open image file.\n");
        return 1;
    }

    // Create a buffer to check through memory card in chunks of 512 bytes
    unsigned char buffer[BLOCK_SIZE];
    // Create a counter to name and keep track of new jpegs
    int jpeg_count = 0;
    // Create an array to store file names in
    char name_the_file[8];
    // Create a new file pointer to save new files to
    FILE *new_jpeg;

    // Read memory card and recover jpegs one at a time
    while (fread(buffer, BLOCK_SIZE, 1, memory_card) == 1)
    {
        // Check for lpeg Header and write new file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (jpeg_count != 0)
            {
                fclose(new_jpeg);
            }
            sprintf(name_the_file, "%03i.jpg", jpeg_count);
            jpeg_count++;
            new_jpeg = fopen(name_the_file, "w");
            fwrite(buffer, BLOCK_SIZE, 1, new_jpeg);
        }
        // Write to current jpeg
        else if (jpeg_count > 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, new_jpeg);
        }
    }
    // Close last open jpeg and memory card
    fclose(new_jpeg);
    fclose(memory_card);
}