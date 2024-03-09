import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    count_save = 0  # Лічильник серіалізацій

    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = Contacts.count_save

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)
        Contacts.count_save += 1

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        # Виключаємо лічильник зі стану об'єкта під час серіалізації
        state = self.__dict__.copy()
        del state['count_save']
        return state

    def __setstate__(self, state):
        # Під час десеріалізації повертаємо лічильник до значення, що було збережено
        self.__dict__.update(state)
        self.count_save = Contacts.count_save
        
        
        

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3
        
        
        
    


