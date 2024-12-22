import cmd
import datetime


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

    prompt = "TaskMngr>>"
    intro = 'Welcome to TaskManagerCLI. type "help" to see all available commands'

    def do_quit(self):
        return True

    def postcmd(self, stop, line):
        print()  # print new line after each command for better readability
        return stop
