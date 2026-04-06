from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "gosell_db"
)

cursor = connection.cursor()

query = """

INSERT INTO vehicle(name,model,running_km,fuel_type,owner_type,place,owner)
VALUES
('Ambassador', '1957 Mark 1', 125000, 'Diesel', 'Second', 'Kunnamkulam', 'Rajesh'),
('Maruti 800', '1984 SS80', 95000, 'Petrol', 'First', 'Thrissur', 'Anoop'),
('Fiat 1100', '1956 Millecento', 643000, 'Petrol', 'Single', 'Ayyanthole', 'Darvin');

"""

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

print("data inserted...")