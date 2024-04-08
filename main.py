'''
main file where things happen
'''
from blockchain_core.blockchain import Blockchain   # importing Blockchain class in blockchain.py file from blockchain_core folder
# imports for database
from blockchain_core.database import init_db, add_block_to_db, load_blockchain_from_db, create_connection
from tests.test_utils import generate_random_transactions
import random
import art

db_file = "data/blockchain.db"
difficulty = 2

def initialize_blockchain(db_file, connection):
    if connection is None:
        connection = create_connection(db_file)
        return connection
    else:
        print("connection exists...")
        loaded_blockchain = load_blockchain_from_db(connection, difficulty)
        if loaded_blockchain and loaded_blockchain.chain:
            print("Loaded existing blockchain from database.")
            return loaded_blockchain
        else:
            print("No existing blockchain found in the database, Creating a new one...")
            new_blockchain = Blockchain(difficulty=difficulty)
            add_block_to_db(connection, new_blockchain.chain[0])
            return new_blockchain

# database example
def main():
    # initialize db and blockchain
    this_connection = init_db(db_file)
    this_blockchain = initialize_blockchain(db_file, this_connection)
    for _ in range(random.randint(1,10)):
        block = this_blockchain.add_block(transactions=generate_random_transactions())
        add_block_to_db(this_connection, block)

    for block in this_blockchain.chain:
        print("-" * 60)
        print(f"Height: {block.height}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Transactions: {block.transactions}")
        print(f"Previous Block Hash: {block.previous_block_hash}")
        print(f"Nonce: {block.nonce}")
        print(f"Current Block Hash: {block.current_block_hash}\n")
        print("-" * 60)

if __name__ == '__main__':
    art.tprint('''blocky blocky
               ...a blockchain''',font="small")
    main()