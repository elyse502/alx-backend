#!/usr/bin/env python3
"""Python Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Dictionary"""

    def put(self, key, item):
        """Puts item in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets item from cache"""
        return self.cache_data.get(key, None)
