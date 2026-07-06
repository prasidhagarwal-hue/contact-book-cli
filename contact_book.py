import json
import os
from contact import Contact

class Contactbook:
    def __init__(self):
        self.filename = "contacts.json"
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
            return [Contact(c["name"], c["phone"], c["email"]) for c in data]

    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()
        print("contact saved successfully")

    def view_all(self):
        if not self.contacts:
            print("no contacts found")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print("contact not found")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                self.save_contacts()
                print("contact deleted successfully")
                return
        print("contact not found")