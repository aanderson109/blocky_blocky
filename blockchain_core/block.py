'''
Contains Block class 
'''
import time
import hashlib
import json

class Block:
    def __init__(self, height, timestamp, transactions, previous_block_hash, nonce):
        self.height = height
        self.timestamp = timestamp if timestamp is not None else time.time()
        self.transactions = transactions
        self.previous_block_hash = previous_block_hash
        self.nonce = nonce
        self.current_block_hash = self.calculate_current_block_hash() # dynamically calculated as part of object init
    
    def calculate_current_block_hash(self):
        '''
        Steps:
            1. Convert Block Data to a String
                + self.__dict__ -> contains all the instance attributes of the block
                + json.dumps() -> converts python dictionary to a json string
                + sort_keys=True -> sorts dictionary keys alphabetically, critical since hashing in a different order would change the hash
                + .encode() -> converts the JSON string into a byte string, necessary since hashing function requires byte data
            2. Generate the Hash
                + hashlib.sha256() -> creates a new sha256 hash object.
                + block_string -> byte string representing the block's contents, passed as input to the hashlib.sha256()
                + hexdigest() -> returns the digest of the data passed to the hashing function as a string of double-length, containing only hexadecimal digits.
        '''
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def __repr__(self):
        return (f"Block (Height: {self.height}, "
                f"Timestamp: {self.timestamp}, "
                f"Transactions: {self.transactions}, "
                f"Previous Block Hash: {self.previous_block_hash}, "
                f"Nonce: {self.nonce}, "
                f"Current Block Hash: {self.current_block_hash})")