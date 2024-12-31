import argon2
import os

def generate_argon2_hash(password, salt_length):
    """
    Generate an Argon2 hash for the given password with a random salt.
    """
    # Generate a random salt
    salt = os.urandom(salt_length)

    # Create an Argon2 password hasher
    hasher = argon2.PasswordHasher()

    # Generate the hash using the specified password and salt
    hash = hasher.hash(password, salt=salt)

    return hash

# Get input from the user
password = input("Enter your password: ")
salt_length = int(input("Enter salt lenght:"))
argon2_hash = generate_argon2_hash(password, salt_length)  # Adjust the salt length as needed
print("Argon2 Hash:", argon2_hash)
