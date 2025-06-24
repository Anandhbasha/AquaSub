class MyController:
    def __init__(self):
        self.tasks = {}  # Simple in-memory dict (task_id : task)

    def create_item(self, item_id, value):
        if item_id in self.tasks:
            return {"status": "fail", "message": "Task ID already exists"}
        self.tasks[item_id] = value
        return {"status": "success", "message": "Task created"}

    def read_item(self, item_id=None):
        if item_id:
            return {item_id: self.tasks.get(item_id, "Task Not Found")}
        return self.tasks  # Return all tasks

    def update_item(self, item_id, value):
        if item_id in self.tasks:
            self.tasks[item_id] = value
            return {"status": "success", "message": "Task updated"}
        return {"status": "fail", "message": "Task not found"}

    def delete_item(self, item_id):
        if item_id in self.tasks:
            del self.tasks[item_id]
            return {"status": "success", "message": "Task deleted"}
        return {"status": "fail", "message": "Task not found"}