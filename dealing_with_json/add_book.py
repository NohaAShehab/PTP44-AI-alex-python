
from inputs_module import  askforInt, askforname, generate_id
from json_handler import  save_book_to_json



def add_new_book():
    title= askforname("Please enter book title: ")
    pages = askforInt("Please enter number of pages: ")
    id = generate_id()
    print(title, pages )
    book_info = {
        "id": id,
        "title": title, "pages":pages
    }
    print(book_info)
    save_book_to_json(book_info)
