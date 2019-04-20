#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, char** argv)
{
    if (argc != 2)
    {
        printf("Usage: ./caesar k");
        return 1;
    }

    int k = atoi(argv[1]);

    if (k < 0)
    {
        printf("key must be positive");
        return 1;
    }

    string plaintext = get_string ("plaintext: ");

    int n = strlen(plaintext);

    printf("ciphertext: ");

    for (int i = 0; i < n; i++)
    {

        if islower(plaintext[i])
        {
            printf("%c",(plaintext[i]-'a'+k) % 26 + 'a');
        }
        else if isupper(plaintext[i])
        {
            printf("%c",(plaintext[i]-'A'+k) % 26 + 'A');
        }
        else if (ispunct(plaintext[i]))
        {
            printf("%c",plaintext[i]);
        }
        else if isspace(plaintext[i])
        {
            printf("%c", plaintext[i]);
        }


    }
    printf("\n");
}