#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // input plaintext and check command-line

    if (argc == 2)
    {
        // checking key function
        if (only_digits(argv[1]))
        {
            string plaintext = get_string("plaintext: ");
            int key = atoi(argv[1]);

            // print ciphertext
            printf("ciphertext: ");
            for (int i = 0, len = strlen(plaintext); i < len; i++)
            {
                printf("%c", rotate(plaintext[i], key));
            }
            printf("\n");
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    else
    {
        printf("Usage: .caesar key\n");
        return 1;
    }
}

// Checking key function
bool only_digits(string s)
{
    for (int i = 0, len = strlen(s); i < len; i++)
    {
        if (isdigit(s[i]) == false)
        {
            return false;
        }
    }
    return s;
}

// Rotate Function
char rotate(char c, int n)
{
    if (isupper(c))
    {
        c = (((int) c + n - 65) % 26) + 65;
    }
    else if (islower(c))
    {
        c = (((int) c + n - 97) % 26) + 97;
    }
    else
    {
        c = c + 0;
    }
    return c;
}
