#!/usr/bin/env python3
""" baseCaching modul """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """ put method """
        if key is None or item is None:
            pass
        else:
            len_num = len(self.cache_data)
            if len_num >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get method """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
