#!/usr/bin/python3

"""N queens puzzle challenge"""

import sys


def print_usage():
    """Prints the usage message."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid(positions, row, col):
    """Check if the queen can be placed at row, col."""
    for i in range(row):
        if positions[i] == col or \
           positions[i] - i == col - row or \
           positions[i] + i == col + row:
            return False
    return True


def solve_nqueens(size, row, positions, solutions):
    """Recursively attempts to place queens on the board and save solutions."""
    if row == size:
        solutions.append(positions[:])
    else:
        for col in range(size):
            if is_valid(positions, row, col):
                positions[row] = col
                solve_nqueens(size, row + 1, positions, solutions)


def format_solution(positions):
    """Formats the solution for printing."""
    # Adjust the column index to be zero-indexed
    formatted_solution = [[row, col] for row, col in enumerate(positions)]
    return formatted_solution


def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        print_usage()

    # Validate N
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Find and print all solutions
    solutions = []
    positions = [-1] * N
    solve_nqueens(N, 0, positions, solutions)

    for solution in solutions:
        print(format_solution(solution))


if __name__ == "__main__":
    main()
