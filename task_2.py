from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):    
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        return self.value.isdigit() and len(self.value) == 10
    
    def __str__(self):
        return f"Phone: {self.value}"

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if (new_phone.validate()):
            self.phones.append(new_phone)    
        else:
            print(f"phone {phone} is not valid.") 

    def delete_phone(self, phone):
        phones = list(filter(lambda x: x.value == phone, self.phones))
        if (len(phones) > 0):
            for p in phones:
                self.phones.remove(p)
            print(f"phone {phone} is successfully removed.") 
        else:
            print(f"phone {phone} is not found.")

    def edit_phone(self, old_phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == old_phone:
                self.phones[i].value = new_phone
                print(f"phone {old_phone} is changed to {new_phone}")

    def find_phone(self, phone):
        phones = list(filter(lambda x: x.value == phone, self.phones))
        if (len(phones) > 0):
            return phone            
          

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        record = self.data.get(name)
        if (record is not None):
            return record
        else:
            print(f"record by name {name} is not found.")
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"The record for name {name} is deleted.")
        
