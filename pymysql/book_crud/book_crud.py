from mysql import connector

class BookListRetriveCreateUpdateDelete:

    def __init__(self):



        try:

            self.connection = connector.connect(

                host = "localhost",
                user = "root",
                password = "Password@123",
                database = "book_db"
            )

            self.cursor = self.connection.cursor()

            print("db connected...")

        except Exception as e:

            print(e)

    def list(self):



        query = "select * from book"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:

            for row in records:

                print(row)

        else:

            print("No records found...")

    def create(self,title=None,author=None,price=None,publisher=None,genre=None,year=None):

    

        query = """

            insert into book(title,author,price,publisher,genre,year) VALUES (%s,%s,%s,%s,%s,%s);

            """
        
        data = (title,author,price,publisher,genre,year)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record inserted...")

    def retrieve(self,id=None):

        query = "select * from book where id = %s"  

        data = (id,)   

        self.cursor.execute(query,data)

        record = self.cursor.fetchone()

        if record:
        
            print(record)

        else:

            print("No record found...")

    def delete(self,id=None):

        query = "delete from book where id = %s"

        data = (id,)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record deleted...")

    def update(self,title=None,id=None):

        query = "update book SET title=%s where id=%s"

        data = (title,id)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record updated")

book_instance = BookListRetriveCreateUpdateDelete()

#book_instance.create("randamoozham","mt",580,"abc","fiction","1997")

# book_instance.retrieve(id=1)
# book_instance.delete(id=1)
book_instance.update("aadu",3)
book_instance.list()