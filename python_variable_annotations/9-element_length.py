#!/usr/bin/env python3
""" Let's write an iterable object """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function with the requested parameters of an iterable object """
    return [(i, len(i)) for i in lst]
