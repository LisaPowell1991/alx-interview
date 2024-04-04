#!/usr/bin/python3

""" A module containing a function, validUTF8 """


def validUTF8(data):
    """
    A method that determines if a given data set
    represents a valid UTF-8 encoding.

    Parameters:
    data: A list of integers, where each int,
    represents one byte of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding,
    else return False.
    """

    count = 0
    for num in data:
        if count == 0:
            if (num >> 5) == 0b110 or (num >> 5 == 0b1110):
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
