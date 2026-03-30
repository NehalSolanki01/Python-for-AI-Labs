# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:53:36 2024

@author: Nehal
"""
#creat book class
class Books:
  def __init__(self,book_title,author_name,pagecount,year_published):
    self.book_title = book_title
    self.author_name = author_name
    self.pagecount = pagecount
    self.year_published = year_published
    self.available = True
    
    #Library has two componenets thats its Name and books that it has.
class Library: 
     def __init__(self, name):
        self.name = name
        self.books = []
          
#activity carried out in library is adding/removing/borrowing and returning books. 
     def add_book(self, book):
        self.books.append(book)
        print(f"{book.book_title} has been added to the library.")
        
     def remove_book(self, book):
        self.books.remove(book)
        print(f"{book.book_title} has been removed from the library.")
        
        
     def borrow_book(self, title):
            for book in self.books:
                if book.book_title == title:
                    if book.available:
                        book.available = False
                    if book.available:
                        book.available = False
                        return f"{book.book_title} has been borrowed"
                        return f"{book.book_title} has been borrowed."
                    else:
                        return f"{book.book_title} is currently not available."
            return f"{title} is not in the library."
               
     def return_book(self, title):
             for book in self.books:
                if book.book_title == title:
                     if not book.available:
                         book.available = True
                         return f"{book.book_title} has been returned successfully."
                     else:
                         return f"{book.book_title} was not borrowed."
             return f"No books are currently availale in {self.name}"

        
        
     
        
        
     def list_available_books(self):
        #with this code we can go through all books available in bibliotheek loosduinen.
        #Check if book in available or not and collect the title from book object.
        #book for book takes only title from book object.
        #Book object have many othe attributes like page count, author etc.
        #book in self.books checks books in library book list
        #if book.avaialble means if book is available in library list
         available_books = [book for book in self.books if book.available]
         if available_books: 
             print(f"Available books in {self.name}:")
             for book in available_books:
                 print(f"{book.book_title}")
         else:
              print(f"This book is currently not availale in {self.name}")                   
         
        
        
        
#create book log
book1 = Books("The Great Gatsby", "F. Scott Fitzgerald", 180, 1925)
book2 = Books("To Kill a Mockingbird", "Harper Lee", 281, 1960)
book3 = Books("1984", "George Orwell", 328, 1949)
book4 = Books("Pride and Prejudice", "Jane Austen", 279, 1813)
book5 = Books("The Catcher in the Rye", "J.D. Salinger", 234, 1951)

#Further create a library and add all bookes to the library
my_library = Library("Bibliotheek Loosduinen")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)
#it throws error that "Library" is not defined. so we will have to create class for ibrary as well.

#Show available books in library
my_library.list_available_books()

#borrow a book
print(my_library.borrow_book("1984"))

#Show list after borrowing
my_library.list_available_books()

#return borrowed book
print(my_library.return_book("1984"))

my_library.list_available_books()

