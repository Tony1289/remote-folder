import hashlib  
import os
import random
import string
def generate_random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))