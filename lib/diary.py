from lib.diary_entry import *
from lib.contact_list import *

class Diary:
    def __init__(self):
        self.all_diary_entries = []
        self.contact_list = ContactList()

    def add(self, entry): # run find_contacts here
        if not isinstance(entry, DiaryEntry):
            raise Exception('This is not a Diary Entry object.')
        self.contact_list.add_contact(entry)
        self.all_diary_entries.append(entry)

    def read_all(self):
        return [entry.format() for entry in self.all_diary_entries]

    def read_entry(self, entry_title):
        return [entry.format() for entry in self.all_diary_entries if entry_title == entry.title][0]

    def select_entry_from_reading_time(self, wpm, minutes):
        if wpm == 0 or minutes == 0:
            raise Exception('The WPM or the minutes available cannot be 0.')
        readable_entries = []
        total_words = wpm * minutes
        for entry in self.all_diary_entries:
            if entry.count_words() <= total_words:
                readable_entries.append(entry)
        readable_entries.sort(key=lambda entry: entry.count_words()) 
        return readable_entries[-1].format()

    def show_todo_list(self, todo_list):
        return todo_list.incomplete()

    def show_contacts(self):
        return self.contact_list.contacts
    
