#!/usr/bin/env python3
""" BaseCaching modul """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ put method """
        if key is None or item is None:
            pass
        else:
            len_num = len(self.cache_data)
            if len_num >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get method """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
