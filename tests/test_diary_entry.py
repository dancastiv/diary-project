from lib.diary_entry import *
# test find contact from one entry
def test_phone_number_extracted_from_entry():
    entry = DiaryEntry('Title2', 'These is a phone number: 07712345678')
    assert entry.find_contacts() == ['07712345678']