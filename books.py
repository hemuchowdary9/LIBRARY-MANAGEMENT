from storage import save_books, load_books
from validation import get_non_empty_input


books = load_books()


def add_book():
    print("\n--- Add Book ---")

    book_id = get_non_empty_input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:
            print("A book with this ID already exists.")
            return

    title = get_non_empty_input("Enter book title: ")
    author = get_non_empty_input("Enter author name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    books.append(book)
    save_books(books)

    print("Book added successfully.")


def view_books():
    print("\n--- Book List ---")

    if len(books) == 0:
        print("No books are available.")
        return

    for book in books:
        print("ID:", book["id"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Status:", book["status"])
        print("------------------------")