#!/usr/bin/env python3
""" function that sums a list of float type numbers """
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ function that adds a list of numbers
        Param:
            input_list(float): floating list of numbers
        Return:
            sum as a float
    """
    suma = 0
    for x in input_list:
        suma += x
    return suma
