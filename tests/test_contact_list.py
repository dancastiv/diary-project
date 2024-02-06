from lib.contact_list import *
from lib.diary_entry import *
# test add one phone number
def test_one_contact_added_to_list():
    contact_list = ContactList()
    entry1 = DiaryEntry('Title', 'Contents')
    entry2 = DiaryEntry('Title2', 'These is a phone number: 07712345678')
    entry3 = DiaryEntry('Another Title', 'But 1122321 is not a phone number')
    contact_list.add_contact(entry2)
    assert contact_list.contacts == ['07712345678']

# test add more than one phone number, but don't accept invalid phone numbers
def test_contacts_added_to_list():
    contact_list = ContactList()
    entry1 = DiaryEntry('Title', '07812345678')
    entry2 = DiaryEntry('Title2', 'These is a phone number: 07712345678')
    entry3 = DiaryEntry('Another Title', 'But 1122321 is not a phone number')
    contact_list.add_contact(entry1)
    contact_list.add_contact(entry2)
    contact_list.add_contact(entry3)
    assert contact_list.contacts == ['07812345678', '07712345678']