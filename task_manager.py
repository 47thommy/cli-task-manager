import cmd
import datetime
import json


class Task:
    def __init__(
        self,
        id,
        description,
    ):
        self.id = id

        self.description = description

        self.status = "todo"
        self.createdAt = datetime.datetime.now().isoformat()
        self.updatedAt = self.createdAt

    def update_description(self, new_description):
        """update the description of the tast"""
        self.description = new_description
        self.updatedAt = datetime.datetime.now().isoformat()

    def update_status(self, new_status):
        """update the status of the task"""
        if new_status in ["todo", "in-progress", "done"]:
            self.status = new_status
            self.updatedAt = datetime.datetime.now().isoformat()

    def to_dict(self):
        """convert the task object to dict"""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }

    @staticmethod
    def from_dict(data):
        """Recreate a Task object from dictionary"""
        task = Task(data["id"], data["description"])
        task.status = data["status"]
        task.createdAt = data["createdAt"]
        task.updatedAt = data["updatedAt"]
        return task


class TaskManagerCLI(cmd.Cmd):
    """cli tool to manage tasks"""

    prompt = "task-cli>>"
    intro = 'Welcome to TaskManagerCLI. type "help" to see all available commands'

    def do_exit(self, line):
        return True

    def do_add(self, description):
        """adds a task to the json file"""

        # first read the json file if it exists and get the latest id
        with open("tasks.json", mode="r", encoding="utf-8") as read_file:
            tasks = json.load(read_file)
        id = tasks[-1].get("id") + 1

        # create the new task and convert it to dectionary
        task_dict = Task(id, description).to_dict()
        # append the new task to the list of tasks
        tasks.append(task_dict)

        # write to the json file with the updates tasks
        with open("tasks.json", mode="w", encoding="utf-8") as write_file:
            json.dump(tasks, write_file)

        print(f"Task {description} added successfully!")

    def do_update(self, arg):
        """updates the task description"""
        parts = arg.split(" ", 1)
        id = int(parts[0])
        description = parts[1].strip('"')

        with open("tasks.json", mode="r", encoding="utf-8") as read_file:
            tasks = json.load(read_file)
        task = Task.from_dict(tasks[id - 1])
        task.update_description(description)
        task_dict = task.to_dict()
        for index, task in enumerate(tasks):
            if task["id"] == id:
                tasks[index] = task_dict
                break
        print(tasks)
        with open("tasks.json", mode="w", encoding="utf-8") as write_file:
            json.dump(tasks, write_file)
        print(f"Task {id} updated successfully!")

    def postcmd(self, stop, line):
        print()  # print new line after each command for better readability
        return stop


if __name__ == "__main__":
    TaskManagerCLI().cmdloop()
