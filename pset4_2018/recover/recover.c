#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

#define buffer_size 512


int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Versuch nocmal\n");
        return 1;
    }

    FILE* infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        fprintf(stderr, "hmmm versuch nochmal\n");
        return 2;
    }


    FILE* outfile = NULL;
    unsigned char buffer[buffer_size];
    char filename[8];
    int counter = 0;

    bool a = false;

    while (fread(buffer, buffer_size, 1, infile))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (a == true)
                fclose(outfile);
            if (a == false)
                a = true;

            sprintf(filename, "%03i.jpg", counter);
            outfile = fopen(filename, "w");
            counter++;
        }
        if (a == true)
        {
            fwrite(&buffer, buffer_size, 1, outfile);
        }

    }
    fclose(infile);
    fclose(outfile);
    return(0);
}