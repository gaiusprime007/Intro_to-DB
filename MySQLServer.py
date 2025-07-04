import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (no database selected yet)
        connection = mysql.connector.connect(
            host='localhost',        # change if different
            user='root',             # change to your MySQL username
            password='Jo$#u@7071**' # change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Try to create the database
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print("Failed to create database:", e)

    except Error as e:
        print("Error connecting to MySQL Server:", e)

    finally:
        # Ensure connection is closed properly
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
