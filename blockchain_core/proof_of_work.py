'''
Proof of work algorithm
'''
import hashlib
import json
import time

def proof_of_work(difficulty, block):
    '''
    simple proof of work algorithm
    - increments the nonce until the hash of the block starts with 'difficulty' number of zeros
    '''
    block.nonce = 0
    computed_hash = block.calculate_current_block_hash()
    while not computed_hash.startswith('0' * difficulty):
        block.nonce += 1
        computed_hash = block.calculate_current_block_hash()
    block.current_block_hash = computed_hash    # updates the block hash after finding the correct nonce
    return True