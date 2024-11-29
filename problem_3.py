import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    return dict(frequency)

def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = code

    generate_huffman_codes(node.left, code + '0', huffman_codes)
    generate_huffman_codes(node.right, code + '1', huffman_codes)

def huffman_encoding(data: str) -> tuple[Optional[str], Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    # Validate input
    if not isinstance(data, str):
        raise ValueError("Input data must be a string.")
    if not data:
        print("No data to encode!")
        return None, None

    frequency = calculate_frequencies(data)

    # Handle single unique character case
    if len(frequency) == 1:
        single_char = next(iter(frequency))
        huffman_codes = {single_char: '0'}
        encoded_data = '0' * len(data)
        return encoded_data, HuffmanNode(single_char, frequency[single_char])

    # Build Huffman tree for other cases
    tree = build_huffman_tree(frequency)

    huffman_codes = {}
    generate_huffman_codes(tree, '', huffman_codes)

    encoded_data = ''.join(huffman_codes[char] for char in data)

    return encoded_data, tree

def huffman_decoding(encoded_data: Optional[str], tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    # Validate input
    if not encoded_data or not tree:
        print("No encoded data or Huffman tree provided!")
        return ""

    # Special case: single character encoding
    if tree.char is not None:
        return tree.char * len(encoded_data)  # Directly decode for single character case

    decoded_text = ''
    current_node = tree

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = tree

    return decoded_text


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2: Repeated characters
    print("\nTest Case 2: Repeated characters")
    sentence = "aaaaaaabbbbbcccd"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 3: Short string
    print("\nTest Case 3: Short string")
    sentence = "abc"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 4: Single repeating character
    print("\nTest Case 4: Single repeating character")
    sentence = "AAAAAAA"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 5: Empty string
    print("\nTest Case 5: Empty string")
    sentence = ""
    encoded_data, tree = huffman_encoding(sentence)
    if encoded_data is None and tree is None:
        print("Encoded: None")
        print("Decoded: None")
        assert sentence == ""
    else:
        print("Error: Empty string not handled correctly!")
