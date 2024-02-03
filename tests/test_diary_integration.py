from lib.diary import *
from lib.diary_entry import *
import pytest

# When an entry is added to the diary, check if it is of the DiaryEntry class. If not, raise exception
def test_diary_entry_class():
    diary = Diary()
    entry1 = DiaryEntry('Title', 'Contents')
    entry2 = ['Fake Title', 'Fake contents']
    diary.add(entry1)
    with pytest.raises(Exception) as e:
        diary.add(entry2)
    error = str(e.value)
    assert error == 'This is not a Diary Entry object.'

# when two entries or moreentries are added to the diary, user can ask for single entries by title
def test_read_entry():
    diary = Diary()
    entry1 = DiaryEntry('Title', 'Contents')
    entry2 = DiaryEntry('Title2', 'These are more contents')
    entry3 = DiaryEntry('Another Title', 'And even more contents')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.read_entry('Title2') == 'Title2: These are more contents'

# given a diary with entries, user can ask for the whole diary 
def test_read_all():
    diary = Diary()
    entry1 = DiaryEntry('Title', 'Contents')
    entry2 = DiaryEntry('Title2', 'These are more contents')
    entry3 = DiaryEntry('Another Title', 'And even more contents')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.read_all() == ['Title: Contents', 'Title2: These are more contents', 'Another Title: And even more contents']

# given a specific reading speed (wpm) and an amount of minutes, user will receive an entry to read
def test_select_entry_from_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Title', 'Contents')
    entry2 = DiaryEntry('Title2', 'These are more contents')
    entry3 = DiaryEntry('Another Title', 'And even more contents which is very cool of course.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.select_entry_from_reading_time(3, 2) == 'Title2: These are more contents'


# if user tries to select entry from reading time and inputs 0 for the wpm or minutes available, raise exception
def test_select_entry_with_0_wpm():
    diary = Diary()
    entry1 = DiaryEntry('Title', 'Contents')
    entry2 = DiaryEntry('Title2', 'These are more contents')
    entry3 = DiaryEntry('Another Title', 'And even more contents')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    with pytest.raises(Exception) as e:
        diary.select_entry_from_reading_time(0, 10)
    error = str(e.value)
    assert error == 'The WPM or the minutes available cannot be 0.'

def test_select_entry_with_0_minutes():
    diary = Diary()
    entry1 = DiaryEntry('Title', 'Contents')
    entry2 = DiaryEntry('Title2', 'These are more contents')
    entry3 = DiaryEntry('Another Title', 'And even more contents')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    with pytest.raises(Exception) as e:
        diary.select_entry_from_reading_time(200, 0)
    error = str(e.value)
    assert error == 'The WPM or the minutes available cannot be 0.'