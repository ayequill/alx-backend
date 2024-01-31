#!/usr/bin/env python3
""" Module for implementing LIFOCaching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Extends BaseCaching and implements the MRU Caching Sys"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.keys.remove(key)
                else:
                    del self.cache_data[self.keys[-1]]
                    print("DISCARD: {}".format(self.keys[-1]))
                    self.keys.pop(-1)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Return value stored in cache_data """
        if key and self.cache_data.get(key):
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data.get(key)

# my_cache = MRUCache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.put("D", "School")
# my_cache.print_cache()
# print(my_cache.get("B"))
# my_cache.put("E", "Battery")
# my_cache.print_cache()
# my_cache.put("C", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
# my_cache.put("H", "H")
# my_cache.print_cache()
# my_cache.put("I", "I")
# my_cache.print_cache()
# my_cache.put("J", "J")
# my_cache.print_cache()
# my_cache.put("K", "K")
# my_cache.print_cache()
