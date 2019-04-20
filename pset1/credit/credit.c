#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long n;
    do
    {
        n = get_long_long ("Number: ");
    }
    while (n < 0);

}