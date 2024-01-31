#!/usr/bin/env python3
"""Python Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCahe class"""

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Put in cache"""
        if key is None or item is None:
            return

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            initial = self.get_first_list(self.queue)
            if initial:
                self.queue.pop(0)
                del self.cache_data[initial]
                print("DISCARD: {}".format(initial))

    def get(self, key):
        """Get form cache"""
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """Moves element"""
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first_list(array):
        """Get first element"""
        return array[0] if array else None
