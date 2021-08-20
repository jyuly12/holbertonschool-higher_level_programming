#!/usr/bin/python3
"""Finds the peak in a list of integers"""


def find_peak(list_of_integers):
    """Defines function that finds the peak number"""
    table = list_of_integers
    value = 0
    if table:
        for i in range(len(table)):
            if i == 1:
                if table[i] > table[i + 1]:
                    value = table[i]
            elif i == len(table) - 1:
                if table[i] > table[i - 1]:
                    value = table[i]
            else:
                if table[i] > table[i + 1] and table[i] > table[i - 1]:
                    value = table[i]
                elif table[i] == table[i + 1] and table[i] == table[i - 1]:
                    value = table[i]
        return value
    else:
        return None
