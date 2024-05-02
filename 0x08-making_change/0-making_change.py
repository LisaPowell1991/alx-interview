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

    # Initialise a list to store the min num of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp[i] if using coin reduces total num of coins needed.
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If total can't be met by any num
    if dp[total] == float('inf'):
        return -1

    return dp[total]
