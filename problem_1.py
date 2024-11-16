from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        self.capacity = max(0, capacity)  # Ensure capacity is non-negative
        self.cache = OrderedDict()

    def get(self, key: int) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        if key in self.cache:
            self.cache.move_to_end(key, last=True)  # Move the accessed item to the end
            return self.cache[key]
        return -1

    def set(self, key: int, value: Any) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        if self.capacity == 0:
            # If capacity is 0, do not store anything
            print("Cache capacity is 0. No items can be stored.")
            return

        if key in self.cache:
            # Update the value and move key to the end
            self.cache.move_to_end(key, last=True)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used key (first key in OrderedDict)
                self.cache.popitem(last=False)
        self.cache[key] = value


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

    # Test Case 2: Cache replacement with small capacity
    small_cache = LRU_Cache(2)
    small_cache.set(1, "a")
    small_cache.set(2, "b")
    assert small_cache.get(1) == "a"  # Returns "a"
    small_cache.set(3, "c")  # Evicts key 2
    assert small_cache.get(2) == -1  # Returns -1
    assert small_cache.get(3) == "c"  # Returns "c"

    # Test Case 3: Edge case with capacity 0
    zero_cache = LRU_Cache(0)
    zero_cache.set(1, "x")  # Should not store anything
    assert zero_cache.get(1) == -1  # Returns -1

    print("All test cases passed!")
