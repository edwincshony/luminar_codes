"""
8. Create a class Book with a constructor that initializes title and author. Display the book details.

"""

class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):

        print(self.title,self.author)

book_inst = Book("Twilight series","Stephenie")
book_inst.display()