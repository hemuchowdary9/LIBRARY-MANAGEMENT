from books import books
from members import members


def library_report():
    print("\n--- Library Report ---")

    total_books = len(books)
    total_members = len(members)

    issued_books = 0
    available_books = 0

    for book in books:
        if book["status"] == "Issued":
            issued_books += 1
        else:
            available_books += 1

    print("Total books:", total_books)
    print("Available books:", available_books)
    print("Issued books:", issued_books)
    print("Total members:", total_members)