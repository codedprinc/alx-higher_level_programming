#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of `n`

    Returns an empty list if `n <= 0`
    You can assume `n` will always be an integer
    """

    if n <= 0:
        return []

    limit = n - 1
    triangle = [[1]]

    for i in range(limit):
        row = []
        row.append(1)

        if len(triangle[i] > 1:
               prev_row_len = len(triangle[i]) - 1
               nxt = 1

               for j in range(prev_row_len):
               suma = triangle[i][j] + triangle[i][nxt]
               row.append(suma)
               nxt += 1

        row.append(1)
        triangle.append(row)

    return triangle
