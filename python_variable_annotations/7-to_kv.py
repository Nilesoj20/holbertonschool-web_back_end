#!/usr/bin/env python3
""" Complex types: string and int / float to tuple """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ annotated function that takes 2 arguments and returns a tuple
        Param:
            k(str): first element of the tuple
            v(tupla): second element of the tuple
        Return:
            a tuple with 2 mixed elements
    """
    return (k, v**2)
