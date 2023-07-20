#LIBRARY MEMBER

import library

class LibraryMember:

    def __init__(self, member_id, name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=['Decolonization of the mind', 'The river between', 'G.O.T']

    def borrow_book(self, Book_object):
        Book_object=input("The Book Object:")
        print("The book object is:", Book_object ,"Is part of"+ str(self.borrowed_books) + "The List")


    def return_book(self, Book_object):
        Book_object=input("The Book Object:")
        print("The book object is:", Book_object ,"Is part of"- str(self.borrowed_books) - "The List")


    def display_info(self):
        print("\n Member ID:", self.member_id)  
        print("\n Name:", self.name)
        print("\n List of Books borrowed:", self.borrowed_books)

Linfo=LibraryMember('BSCIT-01-0008',"JEREMY")


Linfo.borrow_book(32)

Linfo.display_info()