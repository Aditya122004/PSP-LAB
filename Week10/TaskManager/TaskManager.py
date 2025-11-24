from datetime import datetime
class TaskManager:
    def __init__(self):
        self.tasks = {}
    def add_task(self, task_id, task, status="not done"):
        if task_id in self.tasks:
            print("Task already exists")
            return
        self.tasks[task_id] = {
            "task": task,
            "status": status,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print("Task added successfully")
    def mark_done(self, task_id):
        if task_id not in self.tasks:
            print("Task ID not found.")
            return
        self.tasks[task_id]["status"] = "done"
        print("Task marked done")
    def mark_undone(self, task_id):
        if task_id not in self.tasks:
            print("Task ID not found.")
            return
        self.tasks[task_id]["status"] = "not done"
        print("Task marked as not Done")
    def delete_task(self, task_id):
        if task_id not in self.tasks:
            print("Task ID not found.")
            return
        del self.tasks[task_id]
        print("Task Deleted Successfully")
    def list_tasks(self):
        return self.tasks
