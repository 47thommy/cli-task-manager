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

    def get_next_id(self, tasks):
        return max((task["id"] for task in tasks), default=0) + 1

    def get_all_tasks(self):
        """retrieves all tasks from the json file"""
        try:
            with open("tasks.json", mode="r", encoding="utf-8") as read_file:
                tasks = json.load(read_file)
        except FileNotFoundError:
            print("No tasks found. The tasks.json file does not exist.")
            return
        except json.JSONDecodeError:
            print("Error reading tasks. The tasks.json file is corrupted.")
            return
        except Exception as e:
            print(f"unexpected error occurred: {e}")
            return
        return tasks

    def write_to_json_file(self, tasks):
        try:
            with open("tasks.json", mode="w", encoding="utf-8") as write_file:
                json.dump(tasks, write_file)
        except FileNotFoundError:
            print("No tasks found. The tasks.json file does not exist.")
            return
        except json.JSONDecodeError:
            print("Error reading tasks. The tasks.json file is corrupted.")
            return

    def do_exit(self, line):
        return True

    def do_add(self, description):
        """adds a task to the json file"""

        # first read the json file if it exists and get the latest id
        tasks = self.get_all_tasks()
        id = self.get_next_id(tasks)

        # create the new task and convert it to dectionary
        task_dict = Task(id, description).to_dict()
        # append the new task to the list of tasks
        tasks.append(task_dict)

        # write to the json file with the updates tasks
        self.write_to_json_file(tasks)

        print(f"Task {description} added successfully!")

    def do_update(self, arg):
        """updates the task description"""
        parts = arg.split(" ", 1)
        id = int(parts[0])
        description = parts[1].strip('"')

        tasks = self.get_all_tasks()
        task = next((task for task in tasks if task["id"] == id), None)
        if not task:
            print(f"No task found with ID {id}")
        task = Task.from_dict(task)
        task.update_description(description)
        task_dict = task.to_dict()
        for index, task in enumerate(tasks):
            if task["id"] == id:
                tasks[index] = task_dict
                break
        self.write_to_json_file(tasks)
        print(f"Task {id} updated successfully!")

    def do_delete(self, id):
        """deletes a task with the specified id"""
        id = int(id)
        tasks = self.get_all_tasks()
        initial_count = len(tasks)
        tasks = [task for task in tasks if task["id"] != id]
        if len(tasks) == initial_count:
            print(f"No task found with id {id}")
            return
        self.write_to_json_file(tasks)

        print(f"Task {id} deleted successfully!")

    def do_mark_done(self, id):
        """change the status of task with the given id to done"""
        id = int(id)
        tasks = self.get_all_tasks()
        for index, task in enumerate(tasks):
            if task["id"] == id:
                update_task = Task.from_dict(task)
                update_task.update_status("done")
                tasks[index] = update_task.to_dict()
                break
        else:
            print(f"No task found with ID {id}")
            return
        self.write_to_json_file(tasks)
        print(f"Task:{id} status updated to done")

    def do_mark_in_progress(self, id):
        """change the status of task with the given id to in-progress"""
        id = int(id)
        tasks = self.get_all_tasks()

        for index, task in enumerate(tasks):
            if task["id"] == id:
                update_task = Task.from_dict(task)
                update_task.update_status("in-progress")
                tasks[index] = update_task.to_dict()
                break
        else:
            print(f"No task found with ID {id}")
            return

        self.write_to_json_file(tasks)
        print(f"Task:{id} status updated to in-progress")

    def do_list(self, status):
        """list tasks with the the given status if any, or list all tasks if no status is provided"""
        tasks = self.get_all_tasks()
        if status and status not in ["done", "todo", "in-progress"]:
            print(
                'invalid status, you have to choose between "done", "in-progress","todo"'
            )
            return
        if status:
            tasks = [task for task in tasks if task["status"] == status]
        self.format_tasks(tasks)

    def format_tasks(self, tasks):
        """Formats a list of tasks into a table-like structure."""
        if not tasks:
            print("No tasks available.")
            return

        print(
            f"{'ID':<5}{'Description':<30}{'Status':<15}{'Created At':<25}{'Updated At':<25}"
        )
        print("-" * 100)

        for task in tasks:
            print(
                f"{task['id']:<5}"
                f"{task['description']:<30}"
                f"{task['status']:<15}"
                f"{task['createdAt']:<25}"
                f"{task['updatedAt']:<25}"
            )

    def postcmd(self, stop, line):
        print()  # print new line after each command for better readability
        return stop


if __name__ == "__main__":
    TaskManagerCLI().cmdloop()
