#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char* argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        printf("Usage: ./resize n infile outfile\n");
        return 1;
    }

    // factor for resizing the image
    int n = atoi(argv[1]);

    if (n < 1 || n > 100)
    {
       printf("Hol duoc, it should be 0 < n <= 100 \n");
       return 1;
    }

    // remember filenames
    char* infile = argv[2];
    char* outfile = argv[3];

    // open input file
    FILE* inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE* outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    int old_biWidth = bi.biWidth;
    int old_biHeight = bi.biHeight;
    int old_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    bi.biWidth = bi.biWidth * n;
    bi.biHeight = bi.biHeight * n;
    int new_padding =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    bi.biSizeImage = ((bi.biWidth * sizeof(RGBTRIPLE)) + new_padding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int row = 0, old_Height = abs(old_biHeight); row < old_Height; row++)
    {
        for (int i = 0; i < n; i ++)
        {
            // iterate over pixels in scanline           // i am at this place
            for (int column = 0; column < old_biWidth; column++)
            {
                for (int j = 0; j < n; j++)
                {
                    // temporary storage
                    RGBTRIPLE triple;

                    // read RGB triple from infile
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                    // write RGB triple to outfile
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);

                    if (j != (n-1))
                        fseek(inptr, -sizeof(RGBTRIPLE), SEEK_CUR);
                }
            }

            // skip over padding, if any
            fseek(inptr, old_padding, SEEK_CUR);


            for (int l = 0; l < new_padding; l++)
            {
                fputc(0x00, outptr);
            }

            if (i != (n-1))
                fseek(inptr, (-sizeof(RGBTRIPLE) * old_biWidth) - old_padding , SEEK_CUR);

        }

    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    return 0;
}