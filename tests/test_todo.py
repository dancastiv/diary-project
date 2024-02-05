from lib.todo import *
import pytest

# if the user tries to set an empty task, raise exception

def test_empty_task():
    with pytest.raises(Exception) as e:
        task1 = Todo('')
    error = str(e.value)
    assert error == 'Task cannot be blank.'


# if the user sets a task, it now has a string representing the task to be done and self.complete is set to False

def test_task_is_given_todo_class():
    task1 = Todo('Murder Bran Stark')
    assert task1.task == 'Murder Bran Stark'
    assert task1.complete == False

# if user marks task as complete, task's complete property is now set to True
    
def test_complete_property_becomes_true_when_complete():
    task1 = Todo('Murder Bran Stark')
    task2 = Todo('Drink wine menacingly')
    task1.mark_complete()
    assert task1.complete == True
    assert task2.complete == False