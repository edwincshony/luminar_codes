from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "gosell_db"
)

cursor = connection.cursor()

query = """
update vehicle SET place = %s where id = %s;

"""

data = ("kunnamkulam",1)

cursor.execute(query,data)

connection.commit()

print("row updated")