import hashlib
import datetime

class Block:
    """
    A class to represent a block in the blockchain.

    Attributes:
    -----------
    timestamp : datetime.datetime
        The timestamp when the block was created.
    data : str
        The data stored in the block.
    previous_hash : str
        The hash of the previous block in the chain.
    hash : str
        The hash of the current block.
    """

    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str) -> None:
        """
        Constructs all the necessary attributes for the Block object.

        Parameters:
        -----------
        timestamp : datetime.datetime
            The timestamp when the block was created.
        data : str
            The data stored in the block.
        previous_hash : str
            The hash of the previous block in the chain.
        """
        # Ensure that data is not empty
        if not data:
            raise ValueError("Block data cannot be empty.")
        
        self.timestamp: datetime.datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()

    def calc_hash(self) -> str:
        """
        Calculate the hash of the block using SHA-256.

        Returns:
        --------
        str
            The hash of the block.
        """
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        """
        Return a string representation of the block.

        Returns:
        --------
        str
            A string representation of the block.
        """
        return (f"Block(\n"
                f"  Timestamp: {self.timestamp},\n"
                f"  Data: {self.data},\n"
                f"  Previous Hash: {self.previous_hash},\n"
                f"  Hash: {self.hash}\n"
                f")\n")

class Blockchain:
    """
    A class to represent a blockchain.

    Attributes:
    -----------
    chain : list[Block]
        The list of blocks in the blockchain.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Blockchain object.
        """
        self.chain: list[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (the first block in the blockchain).
        """
        # Genesis block has no previous hash and empty data
        genesis_block = Block(datetime.datetime.now(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data: str) -> None:
        """
        Add a new block to the blockchain.

        Parameters:
        -----------
        data : str
            The data to be stored in the new block.
        """
        if not data:
            raise ValueError("Block data cannot be empty.")
        
        previous_block = self.chain[-1]
        new_block = Block(datetime.datetime.now(), data, previous_block.hash)
        self.chain.append(new_block)

    def __repr__(self) -> str:
        """
        Return a string representation of the blockchain.

        Returns:
        --------
        str
            A string representation of the blockchain.
        """
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str

if __name__ == "__main__":
    # Test cases
    # Test Case 1: Create a blockchain and add blocks
    print("Test Case 1: Basic blockchain functionality")
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")
    print(blockchain)

    # Test Case 2: Check the integrity of the blockchain
    print("Test Case 2: Check the integrity of the blockchain")
    for i in range(1, len(blockchain.chain)):
        assert blockchain.chain[i].previous_hash == blockchain.chain[i-1].hash
    print("Blockchain integrity verified.")

    # Test Case 3: Add more blocks and verify
    print("Test Case 3: Add more blocks and verify")
    blockchain.add_block("Block 4 Data")
    blockchain.add_block("Block 5 Data")
    print(blockchain)
    for i in range(1, len(blockchain.chain)):
        assert blockchain.chain[i].previous_hash == blockchain.chain[i-1].hash
    print("Blockchain integrity verified after adding more blocks.")
    
    # Test Case 4: Edge case - Empty data for a block
    print("\nTest Case 4: Edge case - Empty data for a block")
    try:
        blockchain.add_block("")  # Should raise ValueError
    except ValueError as e:
        print(f"Error: {e}")

    # Test Case 5: Edge case - Identical timestamps for blocks
    print("\nTest Case 5: Edge case - Identical timestamps for blocks")
    blockchain.add_block("Block 6 Data")
    blockchain.add_block("Block 7 Data")  # Same timestamp, but different data should still work
    print(blockchain)
    for i in range(1, len(blockchain.chain)):
        assert blockchain.chain[i].previous_hash == blockchain.chain[i-1].hash
    print("Blockchain integrity verified after adding blocks with identical timestamps.")
