#!/usr/bin/env python3
"""
deletion-resilient
"""

import csv
from typing import List, Dict


class Server:
    """ Server class """
    FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ cached data """
        if self.__dataset is None:
            with open(self.FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        def indexed_dataset
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        def get_hyper_index
        """
        dataset = self.indexed_dataset()
        data_num = len(dataset)
        assert 0 <= index < data_num
        res = {}
        data = []
        res['index'] = index
        for i in range(page_size):
            while True:
                curr = dataset.get(index)
                index += 1
                if curr is not None:
                    break
            data.append(curr)

        res['data'] = data
        res['page_size'] = len(data)
        if dataset.get(index):
            res['next_index'] = index
        else:
            res['next_index'] = None
        return res
