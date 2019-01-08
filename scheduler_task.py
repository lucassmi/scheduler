class SchedulerTask:
    def __init__(self, list_task):
        self.list_task = list_task

    def order_task(self):
        self.list_task.sort()

    def run_tasks(self):
        i = 0
        while i < len(self.list_task):
            self.list_task[i].get_string()
            del self.list_task[i]

