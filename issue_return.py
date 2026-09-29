from books import books
from members import members
from storage import save_books
from validation import get_non_empty_input


def issue_book():
    print("\n--- Issue Book ---")

    book_id = get_non_empty_input("Enter book ID: ")
    member_id = get_non_empty_input("Enter member ID: ")

    selected_book = None
    selected_member = None

    for book in books:
        if book["id"] == book_id:
            selected_book = book
            break

    for member in members:
        if member["id"] == member_id:
            selected_member = member
            break

    if selected_book is None:
        print("Book not found.")
        return

    if selected_member is None:
        print("Member not found.")
        return

    if selected_book["status"] == "Issued":
        print("This book is already issued.")
        return

    selected_book["status"] = "Issued"
    save_books(books)

    print("Book issued successfully.")
    print("Book:", selected_book["title"])
    print("Member:", selected_member["name"])


def return_book():
    print("\n--- Return Book ---")

    book_id = get_non_empty_input("Enter book ID: ")

    selected_book = None

    for book in books:
        if book["id"] == book_id:
            selected_book = book
            break

    if selected_book is None:
        print("Book not found.")
        return

    if selected_book["status"] == "Available":
        print("This book has not been issued.")
        return

    selected_book["status"] = "Available"
    save_books(books)

    print("Book returned successfully.")