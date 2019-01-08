class Task:

    def __init__(self, priority, time, name_task):
        self.priority = priority
        self.time = time
        self.name_task = name_task

    def __lt__(self, other):
        return self.priority < other.priority

    def get_time(self):
        return self.time

    def get_priority(self):
        return self.priority

    def get_string(self):
        print("La tâche: {0} avec la priroité {1} s'effectue sur {2} ms".format(self.name_task, self.priority, self.time))

