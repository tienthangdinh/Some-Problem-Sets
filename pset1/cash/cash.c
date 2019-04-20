#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float n;
    int x = 0;
    do
    {
        n = get_float("Change owed:");
    }
    while (n < 0);

    int cents = round(n * 100);

    while (cents >= 25)
    {
        cents = cents - 25;
        x++;
    }
    while (cents >= 10)
    {
        cents = cents - 10;
        x++;

    }
    while (cents >= 5)
    {
        cents -= 5;
        x++;
    }
    while (cents >= 1)
    {
        cents -= 1;
        x++;
    }
    printf("%i\n", x);


}