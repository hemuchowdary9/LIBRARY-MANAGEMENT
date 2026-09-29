from books import add_book, view_books
from members import add_member, view_members
from issue_return import issue_book, return_book
from search import search_book
from reports import library_report

def show_menu():
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Member")
    print("4. View Members")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Search Book")
    print("8. Library Report")
    print("9. Exit")
    print("===============================================")

def main():



    
    while True:
        show_menu()

        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            add_member()

        elif choice == "4":
            view_members()

        elif choice == "5":
            issue_book()

        elif choice == "6":
            return_book()

        elif choice == "7":
            search_book()

        elif choice == "8":
            library_report()

        elif choice == "9":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()