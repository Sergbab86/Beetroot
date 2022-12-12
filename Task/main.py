import json


def create_phonebook(filename="Phonebook.json"):
    with open(filename, mode="a+", encoding="utf-8") as f:
        my_phonebook = {"Phonebook": []}
        my_phonebook_json = json.dumps(my_phonebook)
        f.write(my_phonebook_json)


def add_customer(filename="Phonebook.json"):
    my_dict = {"name": input("Enter Name: "), "surname": input("Enter Surname: "),
               "phone": input("Enter your telephone: "), "city": input("Enter your city: ")}
    with open(filename, mode="a+", encoding="utf-8") as f:

        data = json.load(f.read())
        print(data)


# create_phonebook()
add_customer()
