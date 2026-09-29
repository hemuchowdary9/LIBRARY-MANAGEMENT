from storage import save_members, load_members
from validation import get_non_empty_input


members = load_members()


def add_member():
    print("\n--- Add Member ---")

    member_id = get_non_empty_input("Enter member ID: ")

    for member in members:
        if member["id"] == member_id:
            print("A member with this ID already exists.")
            return

    name = get_non_empty_input("Enter member name: ")
    phone = get_non_empty_input("Enter phone number: ")

    member = {
        "id": member_id,
        "name": name,
        "phone": phone
    }

    members.append(member)
    save_members(members)

    print("Member added successfully.")


def view_members():
    print("\n--- Member List ---")

    if len(members) == 0:
        print("No members are registered.")
        return

    for member in members:
        print("ID:", member["id"])
        print("Name:", member["name"])
        print("Phone:", member["phone"])
        print("------------------------")