
from json_handler import read_all_books, save_all_books
from inputs_module import  askforInt
def remove_book():
    books = read_all_books()
    print(books)
    id = askforInt("please enter book id : ")
    for book in books:
        if book["id"] == id:
            books.remove(book)
            save_all_books(books)

            break

    else:
        print("book not found ")

    # print(books)

