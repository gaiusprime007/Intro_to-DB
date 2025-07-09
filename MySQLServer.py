# import mysql.connector
# from mysql.connector import Error

# def create_database():
#     try:
#         # Connect to MySQL Server 
#         connection = mysql.connector.connect(
#             host='localhost',       
#             user='root',            
#             password='Jo$#u@7071**' 
#         )

#         if connection.is_connected():
#             cursor = connection.cursor()

#             # Try to create the database
#             try:
#                 cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
#                 print("Database 'alx_book_store' created successfully!")
#             except Error as e:
#                 print("Failed to create database:", e)

#     except Error as e:
#         print(mysql.connector.Error, e)

#     finally:
#         # Ensure connection is closed properly
#         if 'cursor' in locals():
#             cursor.close()
#         if 'connection' in locals() and connection.is_connected():
#             connection.close()
#             print("MySQL connection closed.")

# if __name__ == "__main__":
#     create_database()



import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (update user and password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # replace with your actual MySQL root password
        )

        cursor = connection.cursor()

        # Try to create database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")
        finally:
            cursor.close()
            connection.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist and could not be created.")
        else:
            print(f"Connection failed: {err}")

if __name__ == "__main__":
    create_database()
