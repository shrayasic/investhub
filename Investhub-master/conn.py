import mysql.connector
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="25asha28/",
        database="info"
    )
    print("connected", db)

    # Create a cursor object
    cursor = db.cursor()
except mysql.connector.Error as e:
    print(f"Error {e}")
