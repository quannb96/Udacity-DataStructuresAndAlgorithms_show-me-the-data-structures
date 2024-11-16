## Reasoning Behind Decisions:
LRU Cache Implementation: I used an OrderedDict to store the cache. This allows efficient insertion and removal of items while maintaining the order of insertion. The move_to_end() method is used to mark items as recently used, and popitem(last=False) evicts the least recently used item.

Capacity Handling: If the cache is full, the least recently used item is evicted to make space for the new one. If the capacity is zero, no items are stored.

## Time Efficiency:
get(): O(1) - Accessing a key and moving it to the end takes constant time.
set(): O(1) - Insertion and eviction operations are constant time due to the underlying OrderedDict.

## Space Efficiency:
Space Complexity: O(n), where n is the cache capacity. This is because the cache stores up to n key-value pairs.
