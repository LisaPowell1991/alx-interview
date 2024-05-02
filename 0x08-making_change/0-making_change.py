#!/usr/bin/python3

""" A module containing a makeChange function """


def makeChange(coins, total):
    """
    A function that determine the fewest number
    of coins needed to meet a given amount total.

    Args:
    - coins (list): A list of the values of the coins you have.
    - total (int): The amount to be met.

    Returns:
    - int: The fewest number of coins needed to meet total.
    - If total <= 0 return 0.
    - If total can't be met by any num of coins you have return -1.
    """

    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialise the num of coins needed
    num_coins = 0

    # Iterate through each coin value
    for coin in coins:
        while coin <= total:
            total -= coin

            num_coins += 1

    # If total can't be met by any num
    if total != 0:
        return -1

    return num_coins
