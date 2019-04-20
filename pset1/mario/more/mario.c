#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;

    do
    {
        n = get_int("Height: ");
    }
    while (n < 0 || n > 23);

    for (int i = 0; i < n; i++)
    {
        for (int a = 0; a < n-i-1; a++)
        {
            printf(" ");
        }
        for (int b = 0; b < i+1; b++)
        {
            printf("#");
        }
        printf("  ");
        for (int c = 0; c < i+1; c++)
        {
            printf("#");
        }

        printf("\n");
    }
}
