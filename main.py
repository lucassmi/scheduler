from task import Task
from scheduler_task import SchedulerTask

if __name__ == '__main__':
    task_a = Task(1, 20, "job1")
    task_b = Task(2, 10, "job2")
    task_c = Task(3, 30, "job3")
    task_d = Task(5, 15, "job5")
    task_e = Task(4, 30, "job4")

    scheduler = SchedulerTask([task_a, task_b, task_c, task_d, task_e])
    scheduler.order_task()
    scheduler.run_tasks()
