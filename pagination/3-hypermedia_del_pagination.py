#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ method with two arguments that returns a dictionary """
        datos = self.indexed_dataset()
        size = len(datos)
        assert 0 <= index < size
        respuesta = {}
        data = []
        respuesta['index'] = index
        for x in range(page_size):
            while True:
                res = datos.get(index)
                index += 1
                if res is not None:
                    break
            data.append(res)

        response['data'] = data
        response['page_size'] = len(data)
        if datos.get(index):
            respuesta['next_index'] = index
        else:
            respuesta['next_index'] = None
        return respuesta
