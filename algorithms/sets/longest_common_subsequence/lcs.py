#!/usr/bin/env python


def lcs(listX, listY):
    """Dynamic programing version."""
    if not listX or not listY:
        return ""

    matix = []

    for r in range(len(listX) + 1):
        row = []
        for c in range(len(listY) + 1):
            row.append(0)
        matix.append(row)

    # list comprehension version of matix construction
    # matix = [[0 for j in range(len(listY) + 1)] for i in range(len(listX) + 1)]

    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(listX):
        for j, y in enumerate(listY):
            if x == y:
                matix[i + 1][j + 1] = matix[i][j] + 1
            else:
                matix[i + 1][j + 1] = max(matix[i + 1][j], matix[i][j + 1])

    # read the substring out from the matrix
    result = ""
    x, y = len(listX), len(listY)

    while x != 0 and y != 0:
        if matix[x][y] == matix[x - 1][y]:
            x -= 1
        elif matix[x][y] == matix[x][y - 1]:
            y -= 1
        else:
            assert listX[x - 1] == listY[y - 1]
            result = listX[x - 1] + result
            x -= 1
            y -= 1

    return result


def lcs_recursive(listX, listY):
    """Recursive and optimized solution."""
    if not listX or not listY:
        return ""

    x, xs, y, ys = listX[0], listX[1:], listY[0], listY[1:]

    if x == y:
        return x + lcs_recursive(xs, ys)
    else:
        return max(lcs_recursive(listX, ys), lcs_recursive(xs, listY), key=len)
