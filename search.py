from books import books
from validation import get_non_empty_input


def search_book():
    print("\n--- Search Book ---")

    keyword = get_non_empty_input(
        "Enter book title or author: "
    ).lower()

    found = False

    for book in books:
        title = book["title"].lower()
        author = book["author"].lower()

        if keyword in title or keyword in author:
            print("\nBook found")
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            print("------------------------")

            found = True

    if not found:
        print("No book found.")