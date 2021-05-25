#!/usr/bin/python3
"""
This module divides a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    Arg:
        matrix (list):
            item (float or int): elements to divided
        div (float or int): number that divide the matrix
    """
    length = len(matrix[0])

    for row in matrix:
        if length is not len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2)for item in row] for row in matrix]
