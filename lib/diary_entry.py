import re

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.contacts = []

    def format(self):
        return f'{self.title}: {self.contents}'
    
    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())
    
    def find_contacts(self):
        contacts = re.findall(r'\b\d{11}\b', self.contents)
        self.contacts += contacts
        return self.contacts

