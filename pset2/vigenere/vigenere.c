#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char**argv)
{
    if (argc != 2)
    {
        printf("Holla schreib nochmal\n");
        return 1;
    }

    string key = argv[1];
    int keylength = strlen(argv[1]);

    for (int i = 0; i < keylength; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Holla schreib nochmal\n");
            return 1;
        }
    }

    string plaintext = get_string("Plaintext: ");
    int textlength = strlen(plaintext);
    printf("ciphertext: ");

    for (int i = 0, index = 0; i < textlength; i++)
    {
        if isalpha(plaintext[i])
        {
            if (islower(plaintext[i]))
            {
                printf("%c", (plaintext[i]-'a'+toupper(key[index])-'A') % 26 + 'a');
            }
            if (isupper(plaintext[i]))
            {
                printf("%c", (plaintext[i]-'A'+toupper(key[index])-'A') % 26 + 'A');
            }
        }
        else
        {
            printf("%c", plaintext[i]);
        }
        index = (index + 1) % keylength;
    }
    printf("\n");
}