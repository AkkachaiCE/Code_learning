#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    int binaryArr[BITS_IN_BYTE];
    string massage = get_string("Massage: ");
    // printf("%i\n", massage[0]);
    int i = 0;
    while (massage[0] > 0)
    {
        binaryArr[i] = massage[0] % 2;
        massage[0] = massage[0 / 2];
        i++;
    }
    for (int j = i - 1; j >= 0; j--)
    {
        printf("%d", binaryArr[j]);
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
