#!/usr/bin/env python3
""" Complex types - mixed list """
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """  annotated function of complex type list - mixed
        taking a list of integers and floats
        Param:
            mxd_lst(mixed):  list of integers and floats
        Return:
            sum as a float
    """
    suma = 0
    for x in mxd_lst:
        suma += x
    return suma
