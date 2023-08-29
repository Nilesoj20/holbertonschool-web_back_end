#!/usr/bin/env python3
""" Complex types - functions """
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ annotated function takes a multiplier float as an argument
      Param:
        multiplier(float): argument
    Return:
        function that multiplies a float by multiplier
    """
    def make_retorno(x: float) -> float:
        """ function that multiplies a float by multiplier """
        return x * multiplier
    return make_retorno
