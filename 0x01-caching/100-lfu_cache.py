#!/usr/bin/env python3
""" baseCaching module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """ put method """
        if key is None or item is None:
            pass
        else:
            len_num = len(self.cache_data)
            if len_num >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                ll = min(self.frequency.values())
                lfu_ks = []
                for k, val in self.frequency.items():
                    if val == ll:
                        lfu_ks.append(k)
                if len(lfu_ks) > 1:
                    lr_lfu = {}
                    for k in lfu_ks:
                        lr_lfu[k] = self.usage.index(k)
                    dis = min(lr_lfu.values())
                    dis = self.usage[dis]
                else:
                    dis = lfu_ks[0]

                print("DISCARD: {}".format(dis))
                del self.cache_data[dis]
                del self.usage[self.usage.index(dis)]
                del self.frequency[dis]

            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get method """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
