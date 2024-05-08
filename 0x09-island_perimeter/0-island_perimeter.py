#!/usr/bin/python3

""" A module containing a island_perimeter function """


def island_perimeter(grid):
    """
    a Function that calculate the perimeter of a single island in a grid.

    Args:
    - grid (list of lists of int): A 2D grid that represents the island.

    Returns:
    - int: The perimeter of the island.
    """

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    land_cells = 0
    neighbour_cells = 0

    # Iterate through each cell in grid
    for i in range(rows):
        for j in range(cols):

            # if cell is land
            if grid[i][j] == 1:
                land_cells += 1

                # Check the bottom neighbour
                if i < rows - 1 and grid[i + 1][j] == 1:
                    neighbour_cells += 1

                # Check the right neighbour
                if j < cols - 1 and grid[i][j + 1] == 1:
                    neighbour_cells += 1

    # Calculate the perimeter
    return 4 * land_cells - 2 * neighbour_cells
