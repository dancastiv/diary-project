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

```
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

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



"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
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
