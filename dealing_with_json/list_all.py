

from json_handler import read_all_books

def display_all_books():
    books = read_all_books()
    for book in books:
        print(book)