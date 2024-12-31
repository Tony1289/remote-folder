import pyodbc
import hashlib
import getpass


def retrieve_user_credentials():
    try:
        # Connect to the MySQL database using ODBc
        connection = pyodbc.connect('DSN=tony_odbc;UID=root;PWD=root')

        if connection:
            print("Connected to the database successfully.")

            # Create a cursor object
            cursor = connection.cursor()
                  
            # Get input for new user
            action = input("Enter 'a' to add user or 'd' to delete user: ")
            if action == 'a':
                username = input("Enter username: ")
                email = input("Enter email: ")
                password = getpass.getpass("Enter password: ")
                
                # Hash the password
                hashed_password = hashlib.sha3_512(password.encode('utf-8')).hexdigest()
                
                # Insert the new user
                cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
            elif action == 'd':
                username = input("Enter username to delete: ")
                cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            
            # Commit the insert or delete
            connection.commit()
            
            # Close cursor and connection
            cursor.close()
            connection.close()
            print("Database connection closed.")
    except pyodbc.Error as e:
        print("Error while connecting to the database:", e)








# Call the function to retrieve user credentials
retrieve_user_credentials()
