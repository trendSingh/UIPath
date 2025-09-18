import cx_Oracle

def connect_to_oracle_db(username, password, dsn):
    """
    Connect to an Oracle database and return the connection object.
    
    :param username: Database username
    :param password: Database password
    :param dsn: Data Source Name (e.g., 'localhost/orclpdb1')
    :return: Connection object
    """
    try:
        # Establish the database connection
        connection = cx_Oracle.connect(username, password, dsn)
        print("Successfully connected to the database")
        return connection
    except cx_Oracle.DatabaseError as e:
        # Handle the database connection error
        error, = e.args
        print(f"Error connecting to the database: {error.message}")
        return None

def main():
    # Database connection details
    username = 'your_username'
    password = 'your_password'
    dsn = 'localhost/orclpdb1'  # Update with your database server details
    
    # Connect to the database
    connection = connect_to_oracle_db(username, password, dsn)
    
    # Perform further database operations using the connection object
    # ...
    
    # Close the connection
    if connection:
        connection.close()
        print("Database connection closed")

if __name__ == "__main__":
    main()