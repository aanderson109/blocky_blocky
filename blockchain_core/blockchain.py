'''
Contains Blockchain class
'''
from blockchain_core.block import Block
import time
from blockchain_core.proof_of_work import proof_of_work

class Blockchain:
    def __init__(self, difficulty, create_genesis=True):
        self.chain = []
        self.difficulty = difficulty
        if create_genesis:
            self.genesis_block = self.create_genesis_block()
    
    def create_genesis_block(self):
        """
        create the first block in the blockchain with a predefined previous hash
        """
        genesis_block = Block(height=0, timestamp=time.time(), transactions="Genesis Block", previous_block_hash=None, nonce=0)
        self.chain.append(genesis_block)
    
    def add_block(self, transactions):
        """
        adds a new block to the chain after finding the correct nonce
        """
        previous_block = self.last_block
        new_block = Block(len(self.chain), timestamp=time.time(), transactions=transactions, previous_block_hash=previous_block.current_block_hash, nonce=0)
        
        # perform the proof of work for the new block
        proof_of_work(self.difficulty, new_block)

        # once the proof of work is complete, append the block to the chain
        self.chain.append(new_block)
        return new_block    # return new block so it can be used for other things
    
    @property   # marks method as a property, allowing us to access it as if it were an attribute
    def last_block(self):
        return self.chain[-1]