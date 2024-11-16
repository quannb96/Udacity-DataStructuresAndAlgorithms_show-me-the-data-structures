## Reasoning Behind Decisions:
Block Structure: Each block stores a timestamp, data, previous block’s hash, and its own hash (calculated with SHA-256), ensuring data integrity and security.
Genesis Block: The first block has no previous hash ("0") and fixed data, initializing the blockchain.
Hash Calculation: The block’s hash depends on its data and the previous block’s hash, ensuring immutability.


## Time Efficiency:
calc_hash: O(1), since SHA-256 is constant time.
add_block: O(1) for adding a block, including hash calculation.
Overall: O(n) for rendering the blockchain as n is the number of blocks.


## Space Efficiency:
Space Complexity: O(n), where n is the number of blocks in the chain. The space grows linearly with the number of blocks added.