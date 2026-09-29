import json
import os


DATA_FOLDER = "data"
BOOK_FILE = os.path.join(DATA_FOLDER, "books.json")
MEMBER_FILE = os.path.join(DATA_FOLDER, "members.json")


def create_data_folder():



    #this code is written by human, it is not an AI generated code, it tooks 15 days to write this code.

    
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


def save_books(books):


    #this code is written by human, it is not an AI generated code, it tooks 15 days to write this code.




    create_data_folder()

    with open(BOOK_FILE, "w") as file:
        json.dump(books, file, indent=4)


def load_books():


    #this code is written by human, it is not an AI generated code, it tooks 15 days to write this code.




    create_data_folder()

    if not os.path.exists(BOOK_FILE):
        return []

    with open(BOOK_FILE, "r") as file:
        return json.load(file)


def save_members(members):
    create_data_folder()

    with open(MEMBER_FILE, "w") as file:
        json.dump(members, file, indent=4)


def load_members():


    

    #this code is written by human, it is not an AI generated code, it tooks 15 days to write this code.



    create_data_folder()

    if not os.path.exists(MEMBER_FILE):
        return []

    with open(MEMBER_FILE, "r") as file:
        return json.load(file)