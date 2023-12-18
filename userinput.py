# userinput.py
import json

def get_user_input():
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    # Add more fields as needed

    user_data = {
        "name": name,
        "phone_number": phone_number,
        # Add more fields as needed
    }

    with open("user_data.json", "w") as file:
        json.dump(user_data, file)

if __name__ == "__main__":
    get_user_input()
