#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // TODO
    int c;
    do
    {
        c = get_int("Change owed: ");
    }
    while (c < 0);
    return c;
}

int calculate_quarters(int cents)
{
    // TODO
    int cq = 0;
    cq = cents / 25;
    if (cq >= 1)
    {
        return cq;
    }
    else
    {
        return 0;
    }
}

int calculate_dimes(int cents)
{
    // TODO
    int cd = 0;
    cd = cents / 10;
    if (cd >= 1)
    {
        return cd;
    }
    else
    {
        return 0;
    }
}

int calculate_nickels(int cents)
{
    // TODO
    int cn = 0;
    cn = cents / 5;
    if (cn >= 1)
    {
        return cn;
    }
    else
    {
        return 0;
    }
}

int calculate_pennies(int cents)
{
    // TODO
    return cents;
}
