#!/usr/bin/python3
"""
This script contains a function to generate Pascal's triangle up to n rows.
"""


def generate_pascals_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = []
    for row_number in range(n):
        # Initialize the row with 1's
        row = [1] * (row_number + 1)

        if row_number >= 2:
            # Calculate the values in the row based on the previous row
            for j in range(1, row_number):
                row[j] = triangle[row_number - 1][j - 1] + triangle[row_number - 1][j]

        triangle.append(row)

    return triangle