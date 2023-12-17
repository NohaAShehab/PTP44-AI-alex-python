import  json


def read_all_books():
    try:
        myobj = open("books.json",'r' )
    except Exception:
        return False
    else:
        try:
            data = json.load(myobj)
        except Exception as e:
            print(e)
            myobj.close()
            return []
        else:
            return data

def save_all_books(books):
    try:
        myobj = open('books.json', 'w')
    except Exception as e:
        print(e)
    else:
        json.dump(books, myobj, indent=4)
        return True


def save_book_to_json(book_details):
    all_books = read_all_books()
    print(all_books, type(all_books))
    all_books.append(book_details)
    save_all_books(all_books)
    # try:
    #     myobj = open('books.json', 'w')
    # except Exception as e:
    #     print(e)
    # else:
    #     json.dump(all_books, myobj, indent=4)
    #     return True


if __name__ == "__main__":
    print(read_all_books())