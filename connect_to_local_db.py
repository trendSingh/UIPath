import sqlite3
from getpass import getpass

def get_database_credentials():
    """
    Prompts the user to enter the database credentials.
    """
    db_name = input("Enter the name of the database: ")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    return db_name, username, password

def connect_to_database(db_name, username, password):
    """
    Connects to the SQLite database using the provided credentials.

    Parameters:
    db_name (str): The name of the database.
    username (str): The username for the database.
    password (str): The password for the database.

    Returns:
    connection: SQLite3 database connection object.
    """
    try:
        # Establish the connection to the database
        connection = sqlite3.connect(db_name)

        # Here we just print the username and password for demonstration
        # In a real case, you should use these credentials as needed
        print(f"Successfully connected to the database '{db_name}' using username '{username}'.")

        return connection
    except sqlite3.Error as error:
        print(f"Error while connecting to database: {error}")
        return None

def main():
    """
    Main function to execute the database connection process.
    """
    db_name, username, password = get_database_credentials()
    connection = connect_to_database(db_name, username, password)

    if connection:
        # You can perform database operations here
        # For example: cursor = connection.cursor()
        
        # Close the connection
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()