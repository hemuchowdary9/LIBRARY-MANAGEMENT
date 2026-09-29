def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("This field cannot be empty.")


def get_number_input(message):
    while True:
        value = input(message).strip()

        if value.isdigit():
            return value

        print("Please enter numbers only.")


def confirm_action(message):
    while True:
        answer = input(message + " (y/n): ").lower().strip()

        if answer == "y":
            return True

        if answer == "n":
            return False

        print("Please enter y or n.")