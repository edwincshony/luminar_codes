#vehicle(id,name,model,running_km,fuel_type,owner_type,place,owner)

from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "gosell_db"
)

cursor = connection.cursor()

query = """

create table vehicle (

id int auto_increment primary key,
name varchar(200) not null,
model varchar(200) not null,
running_km int not null,
fuel_type varchar(200) not null,
owner_type varchar(200) not null,
place varchar(200) not null,
owner varchar(200) not null 
);

"""

cursor.execute(query)

connection.commit()

cursor.close()
connection.close()

print("table created...")