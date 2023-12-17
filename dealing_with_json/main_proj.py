from add_book import  add_new_book
from list_all import display_all_books
from delete_book import remove_book

def mainmenu():
    print("---------- Welcome to iti book store ------------")
    while True:
        print("\n\n")
        choice = input("please enter your choice")
        if choice=='c':
            add_new_book()
        elif choice=='e':
            exit()
        elif choice=='l':
            display_all_books()
        elif choice == 'd':
            remove_book()

        else:
            print("---- please enter valid choice ")


if __name__ == '__main__':
    mainmenu()