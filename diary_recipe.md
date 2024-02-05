# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_


_Also design the interface of each class in more detail._

```python

class Diary:
    def __init__(self):
        # initializes list of diary entries
        pass

    def add(self, entry):
        # parameters: entry - an instance of Entry
        # run find_contacts here
    
    def read_all(self):
        # Returns: List of diary entries (entire diary)

    def read_entry(self, entry)
        # parameters entry - instance of entry (title?)
        # returns: specified entry

    def select_entry_from_wpm(self, wpm, minutes)
        # parameters:
        #   wpm: int representing words per minute the user can read
        #   minutes: int representing minutes the user has available for reading

    def show_todo_list(self):
    # returns: Todo List (from todo class)

    def show_contacts(self):
    # returns Contact list (from contacts class)

    def find_contacts(self):
        # if there is a contact in an entry, add to phone book


class DiaryEntry:
    def __init__(self):
        pass

    def create(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        pass

class TodoList:
    def __init__(self):
        # initialize todo list
        pass

    def add(self, task):
        # Parameters:
        #   task: instance of task
    
    def complete(self):
        # return: list of completed tasks

    def incomplete(self):
        # return: list of incomplete tasks

class Todo:
    def __init__(self, task):
        # task 
        # set completed to False
        pass

    def set_completed(self)
        # set completed to True

class PhoneBook:
    def __init__(self):
        # initialize phonebook list





```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

# When an entry is added to the diary, check if it is of the DiaryEntry class. If not, raise exception

diary = Diary()
entry1 = DiaryEntry('Title', 'Contents')
isinstance(entry1, DiaryEntry) => True

# when two entries or moreentries are added to the diary, user can ask for either the whole diary or single entries by title

diary = Diary()
entry1 = DiaryEntry('Title', 'Contents')
entry2 = DiaryEntry('Title2', 'These are more contents')
entry3 = DiaryEntry('Another Title', 'And even more contents')
diary.read_entry('Title2') => 'Title2: These are more contents

# given a specific reading speed (wpm) and an amount of minutes, user will receive an entry to read
diary = Diary()
entry1 = DiaryEntry('Title', 'Contents')
entry2 = DiaryEntry('Title2', 'These are more contents')
entry3 = DiaryEntry('Another Title', 'And even more contents')
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.find_entry_to_read(5, 1) => 'Title2: These are more contents'

# when user adds multiple todo tasks to todo list, they can request the full list
diary = Diary()
todo_list = TodoList()
task1 = Todo('Murder Bran Stark')
task2 = Todo('Drink wine menacingly')
task3 = Todo('Make Aurane Waters master of ships')
todo_list.add(task1)
todo_list.add(task2)
todo_list.add(task3)
diary.show_todo_list() => [task1, task2, task3]

# when user adds a diary entry that includes a phone number, the number will be extracted and added to the phone book
diary = Diary()
contacts = ContactList()
entry1 = DiaryEntry('Title', 'Contents')
entry2 = DiaryEntry('Title2', 'These is a phone number: 07712345678')
entry3 = DiaryEntry('Another Title', 'But 1122321 is not a phone number')
todo_list.add(task1)
todo_list.add(task2)
todo_list.add(task3)
diary.show_contacts => ['07712345678']

# given a phonebook with entries, user will receive a full phonebook






```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
