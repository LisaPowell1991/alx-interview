#!/usr/bin/python3

""" Pascal's triangle """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified num of rows.
    First and last element of each row is always 1.

    Parameters:
    - n (int): Num of rows in the Pascal's triangle.

    Returns:
    - List of lists of int: List of lists representing Pascal's triangle.
    - Or returns an empty list if n <= 0.
    """

    if n <= 0:
        return []

    triangle = []

    for row_num in range(n):
        row = [1]
        if row_num > 0:
            prev_row = triangle[-1]
            for col_num in range(1, row_num):
                # Calculate the value by summing the two numbers above
                new_value = prev_row[col_num - 1] + prev_row[col_num]
                row.append(new_value)
            row.append(1)
        triangle.append(row)

    return triangle
