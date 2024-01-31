#!/usr/bin/env python3
""" Module for implemting basic caching """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """

    def put(self, key, item):
        """ Adds values to cache_data """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets the value from cache_data """
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)

#
# my_cache = BasicCache()
# my_cache.print_cache()
# my_cache.put("A", "Hello")
# my_cache.put("B", "World")
# my_cache.put("C", "Holberton")
# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# print(my_cache.get("D"))
# my_cache.print_cache()
# my_cache.put("D", "School")
# my_cache.put("E", "Battery")
# my_cache.put("A", "Street")
# my_cache.print_cache()
# print(my_cache.get("A"))
