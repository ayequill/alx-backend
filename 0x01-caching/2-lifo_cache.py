#!/usr/bin/env python3
""" Module for implementing LIFOCaching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class to implement FIFO caching system """

    def __init__(self):
        """ Initialize class instance. """
        super().__init__()

    def put(self, key, item):
        """ Add key/value pair to cache_data """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last = sorted(self.cache_data)[-1]
                self.cache_data.pop(last)
                print("DISCARD: {}".format(last))
            self.cache_data[key] = item

    def get(self, key):
        """ Return value stored in cache_data """
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)


# my_cache = LIFOCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
