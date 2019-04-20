#include <cs50.h>
#include <stdio.h>

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
        for (int b = 0; b < n - 1 - i; b++)
        {
            printf(" ");
        }
        for (int a = 0; a < i + 2; a++)
        {
            printf("#");
        }
        printf("\n");
    }
}