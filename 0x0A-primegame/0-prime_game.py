#!/usr/bin/python3

""" A module containing a isWinner function """


def isWinner(x, nums):
    """
    Determine the winner of each game round.
    Args:
    x (int): Number of rounds.
    nums (list): List of integers, where each integer n,
    represents the upper limit of the set of each round.
    Returns:
    str: The name of the player that won the most rounds,
    OR None if the result is a tie.
    """

    def sieve(n):
        """
        Generate a list of prime nums up to n,
        using the Sieve of Eratosthenes.
        Args:
        n (int): The upper limit to generate prime nums.
        Returns:
        list: A list of prime nums up to n.
        """
        primes = [True for _ in range(n + 1)]
        p = 2

        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primes[p]]

    # Check for invalid input
    if x <= 0 or not nums:
        return None

    # Variables to count the num of wins for Maria and Ben
    mariaWins = 0
    benWins = 0

    # Simulate each round
    for n in nums:
        primes = sieve(n)
        turn = 0

        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            turn += 1

        if turn % 2 == 0:
            benWins += 1
        else:
            mariaWins += 1

    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
