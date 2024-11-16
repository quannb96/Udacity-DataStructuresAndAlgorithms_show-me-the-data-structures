
## Reasoning Behind Decisions:
Huffman Coding: Compresses data by assigning shorter codes to frequent characters using a Huffman tree.
Min-Heap: A priority queue builds the tree by combining nodes with the least frequencies, placing frequent characters near the root.

## Time Efficiency:
Time Complexity:
calculate_frequencies: O(n)
build_huffman_tree: O(n log n)
generate_huffman_codes: O(n)
Overall: O(n log n)

## Space Efficiency:
Space Complexity: O(n) for frequencies, tree, and encoded data.
