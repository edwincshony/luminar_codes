from mysql import connector

# step1: establish a connection connector > connect()

connection=connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123"
)

print(connection)

cursor = connection.cursor()  # cursor object create

query = "create database py_db" # write the mysql query in string

cursor.execute(query)

connection.commit() # only required for write operations (like making any change in db)

print("completed")