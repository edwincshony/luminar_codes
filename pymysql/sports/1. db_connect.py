from mysql import connector

# step1: establish a connection connector > connect()

connection=connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123"
)

print(connection)

