from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "gosell_db"
)

cursor = connection.cursor()

query = "delete from vehicle where id = %s"

data = (3,)

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()

print("record deleted")