#!/usr/bin/env python3
""" BaseCaching """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """

    def __init__(self):
        """ Initialize the class """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ put method """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ get method """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
