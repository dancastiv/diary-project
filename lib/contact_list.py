import lib.diary_entry

class ContactList():
    def __init__(self):
        self.contacts = []

    def add_contact(self, entry):
        self.contacts += entry.find_contacts()
