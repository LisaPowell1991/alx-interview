#!/usr/bin/python3

""" A module containing a function, minOperations. """


def minOperations(n):
    """
    Calculate the min number of operations needed to
    obtain n 'H' characters in the file.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The min number of operations required
    to achieve exactly n 'H' characters.
    Or return 0 if n is less than 2.
    """

    if n < 2:
        return 0

    operations = 0
    factor = 2

    # Loop until is reduced to 1
    while n > 1:

        # Find the smallest factor of n
        while n % factor == 0:

            # Add the factor to operations and reduce n
            operations += factor
            n //= factor

        factor += 1

    return operations
