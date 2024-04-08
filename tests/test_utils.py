import random
import string

def generate_random_transactions(length=10):
    '''
    generates a random string of fixed length
    '''
    letters = string.ascii_letters + string.digits  #includes both letters and numbers
    return ''.join(random.choice(letters) for i in range(length))