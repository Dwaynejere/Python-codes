#LIBRARY MANAGEMENT SYSTEM
class Book:

    def __init__(self, title, author, publication_year, borrowed):
        self.title=title
        self.author=author
        self.publication_year=publication_year
        self.borrowed=borrowed 

    def borrow_book(self):
          self.borrowed=input("Enter No. Books entered:")
          if self.borrowed == True:
           print("The the Book is borrowed")
       

    def return_book(self):
        
            print("Book has been returned:", bool(self.borrowed!=self.borrowed))


    def display_info(self):
        print("The Title of the book:", self.title)
        print("\n The Author of the Book:", self.author)
        print("\n The Publication year of this Book:", self.publication_year)
        print("\n Status of the book:",self.borrowed)


Library=Book('Decolinising of the mind', 'Ngugi Wa Thiongo', '12/6/1984', True)

Library.borrow_book()


Library.return_book()


Library.display_info()