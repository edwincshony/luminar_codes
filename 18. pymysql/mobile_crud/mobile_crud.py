# mobile[id,title,brand,specs,price]

from mysql import connector

class MobileListRetriveCreateUpdateDelete:

    def __init__(self):
        
        self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password = "Password@123",
            database = "mobile_db"
        )

        self.cursor = self.connection.cursor()

        print("database connected...")

    def list(self):

        query = "select * from mobile"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        if record:

            for row in record:
                print(row)
            
        else:

            print("no records...")

    def create(self,title=None,brand=None,specs=None,price=None):
        query = """

        INSERT INTO mobile(title,brand,specs,price) VALUES (%s,%s,%s,%s);

        
        """
        data = (title,brand,specs,price)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("inserted...")

    def retrieve(self,id=None):

        query = "select * from mobile where id = %s";
        data = (id,)
        self.cursor.execute(query,data)
        record = self.cursor.fetchone()
        print(record)


    def delete(self,id=None):

        query = "delete from mobile where id=%s"

        data = (id,)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record deleted")

    
mobile_instance = MobileListRetriveCreateUpdateDelete()
mobile_instance.list()
#mobile_instance.create("Motorola G86 Power","Motorola","8GB ram 16 rom",16000)
#mobile_instance.retrieve(id=1)
#mobile_instance.delete(id=1)
# mobile_instance.update(title="G86 Power",id=3)
