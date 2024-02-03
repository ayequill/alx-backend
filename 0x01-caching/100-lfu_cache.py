#!/usr/bin/env python3
"""Module for implementing LFUCaching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class to implement LFU caching system"""

    def __init__(self):
        """Initialize class instance."""

        super().__init__()
        self.cache_order = []
        self.key_frequency = {}

    def put(self, key, item):
        """Add key/value pair to cache_data. If the number of items in"""

        if key and item:
            current_size = len(self.cache_data)

            if current_size >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                least_frequent = min(self.key_frequency.values())
                least_frequent_keys = [k for k, v in self.key_frequency.items() if v == least_frequent]

                if len(least_frequent_keys) > 1:
                    lru_lfu = {lfu_key: self.cache_order.index(lfu_key) for lfu_key in least_frequent_keys}
                    key_to_discard = min(lru_lfu, key=lru_lfu.get)
                else:
                    key_to_discard = least_frequent_keys[0]

                print("DISCARD: {}".format(key_to_discard))
                del self.cache_data[key_to_discard]
                self.cache_order.remove(key_to_discard)
                del self.key_frequency[key_to_discard]

            if key in self.key_frequency:
                self.key_frequency[key] += 1
            else:
                self.key_frequency[key] = 1

            if key in self.cache_order:
                self.cache_order.remove(key)

            self.cache_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Function that returns value from dictionary (cache)"""

        if key is not None and key in self.cache_data:
            self.cache_order.remove(key)
            self.cache_order.append(key)
            self.key_frequency[key] += 1

            return self.cache_data[key]
        return None


# my_cache = LFUCache()
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
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# print(my_cache.get("I"))
# print(my_cache.get("H"))
# my_cache.put("J", "J")
# my_cache.print_cache()
# my_cache.put("K", "K")
# my_cache.print_cache()
# my_cache.put("L", "L")
# my_cache.print_cache()
# my_cache.put("M", "M")
# my_cache.print_cache()
