class Todo:
    def __init__(self, task):
        if task == '':
            raise Exception('Task cannot be blank.')
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True