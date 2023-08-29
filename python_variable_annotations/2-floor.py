#!/usr/bin/env python3
""" type-annotated function floor which takes a float n as argument """
import math


def floor(n: float) -> int:
    """Calculates and returns the floor of a floating-point number
        Param:
            n(float): floating point number
        Return:
            the floor of the float
    """
    return math.floor(n)
