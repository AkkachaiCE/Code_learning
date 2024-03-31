// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill_amount, float tax_percent, int tip_percent);
float am = 0;

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// TODO: Complete the function
float half(float bill_amount, float tax_percent, int tip_percent)
{
    am = ((bill_amount * (1 + tax_percent / 100.0)) * (1 + tip_percent / 100.0)) / 2.0;
    return am;
}
