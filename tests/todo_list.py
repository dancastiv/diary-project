class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, task):
        self.todo_list.append(task)

    def incomplete(self):
        incomplete_tasks = [task for task in self.todo_list if task.complete == False]
        return incomplete_tasks

    def complete(self):
        complete_tasks = [task for task in self.todo_list if task.complete == True]
        return complete_tasks

    def give_up(self):
        [task.mark_complete() for task in self.todo_list]
        self.complete()
