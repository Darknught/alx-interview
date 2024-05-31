#!/usr/bin/python3
""" How to implement pascal's triangle. """


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of list of int: A list of lists where each
        sublist represents a row in Pascal's Triangle.
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the Pascal's Triangle with the first row
    triangle = [[1]]

    # Loop to generate rows from the 2nd row up to the nth row
    for i in range(1, n):
        row = [1]  # Start each new row with a 1

        # Loop to calculate the values for the current row
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End each row with a 1
        row.append(1)

        # Append the newly created row to the triangle
        triangle.append(row)

    # Return the complete Pascal's Triangle up to the nth row
    return triangle
