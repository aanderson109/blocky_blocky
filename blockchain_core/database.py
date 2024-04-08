'''
functions necessary for interacting with SQL database to setup persistance
'''
import sqlite3
from sqlite3 import Error
from blockchain_core.blockchain import Blockchain
from blockchain_core.block import Block

def create_connection(db_file):
    '''
    Creates a database connection to the sqlite database (db_file)
    '''
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    
    return connection

def create_table(connection, create_table_sql):
    """
    Create a table from the create_table_sql statement
    """
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_block_to_db(connection, block):
    """
    Add a block to the blocks table
    """
    sql = ''' INSERT INTO blocks(height, timestamp, transactions, previous_block_hash, nonce, current_block_hash)
              VALUES (?,?,?,?,?,?) '''
    cur = connection.cursor()

    # assuming block.transactions is already a JSON string or similar serializable format
    cur.execute(sql, (block.height, block.timestamp, block.transactions, block.previous_block_hash, block.nonce, block.current_block_hash))
    connection.commit()
    return cur.lastrowid

def load_blockchain_from_db(connection, difficulty):
    """
    query all rows in the blocks table
    """
    cur = connection.cursor()
    cur.execute("SELECT * FROM blocks ORDER BY height ASC")

    rows = cur.fetchall()
    blockchain = Blockchain(difficulty)
    for row in rows:
        block_data = row[:-1] # excludes current_block_hash from constructor unpacking
        block = Block(*block_data)
        block.current_block_hash = row[-1]
        # creates Block instance from row data
        blockchain.chain.append(block)
    
    return blockchain

# SQL for creating the blocks table
create_blocks_table_sql = """CREATE TABLE IF NOT EXISTS blocks (
                            height integer PRIMARY KEY,
                            timestamp text NOT NULL,
                            transactions text,
                            previous_block_hash text,
                            nonce integer,
                            current_block_hash text
                        );"""

def init_db(db_file):
    # create database connection
    connection = create_connection(db_file)

    # create blocks table
    if connection is not None:
        create_table(connection, create_blocks_table_sql)
    else:
        print("Error! cannot create the database connection")
    
    return connection