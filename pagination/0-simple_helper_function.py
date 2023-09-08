#!/usr/bin/env python3
""" Simple auxiliary function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ start and end index corresponding to the range of indexes """
    inicio = 0
    fin = 0
    for x in range(page):
        inicio = fin
        fin += page_size
    return (inicio, fin)
