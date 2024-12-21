import cmd


class TaskManagerCLI(cmd.Cmd):
    """cli tool to manage tasks"""

    prompt = "TaskMngr>>"
    intro = 'Welcome to TaskManagerCLI. type "help" to see all available commands'

    def do_quit(self):
        return True

    def postcmd(self, stop, line):
        print()  # print new line after each command for better readability
        return stop
