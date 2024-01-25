#!/usr/bin/env python3
""" Python Module """
import csv
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a Tuple """

    start = (page - 1) * page_size
    end = page * page_size

    return start, end


class Server:
    """ Paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Pagination of dataset """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        self.dataset()

        if self.__dataset is None:
            return []

        idx_range = index_range(page, page_size)
        data = self.__dataset[idx_range[0]:idx_range[1]]
        return data
