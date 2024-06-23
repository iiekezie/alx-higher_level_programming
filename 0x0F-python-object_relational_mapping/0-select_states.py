#!/usr/bin/python3

import MySQLdb

if __name__ == "__main__":
    """
    Connects to a MySQL database and retrieves all states from the 'states' table,
    ordered by id in ascending order. Prints the results.
    """
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter database name: ")

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query to get all states ordered by id
        sql = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(sql)

        # Fetch all results
        results = cursor.fetchall()

        # Print results
        for row in results:
            print(row)

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()