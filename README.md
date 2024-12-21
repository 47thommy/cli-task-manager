# Task Tracker CLI

Task Tracker is a simple Command Line Interface (CLI) application to track and manage tasks. It helps users keep track of their tasks by categorizing them into "To Do," "In Progress," and "Done." The application stores tasks in a JSON file, making it easy to use and lightweight.

## Features

- Add tasks with descriptions
- Update task descriptions
- Delete tasks
- Mark tasks as "In Progress" or "Done"
- List all tasks
- List tasks by status (To Do, In Progress, Done)

## Task Properties

Each task has the following properties:

- **id**: A unique identifier for the task
- **description**: A short description of the task
- **status**: The current status of the task ("todo", "in-progress", "done")
- **createdAt**: The date and time the task was created
- **updatedAt**: The date and time the task was last updated

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/47thommy/cli-task-manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd cli-task-manager
   ```

3. Ensure python is installed.

4. Make the CLI executable (if applicable):
   ```bash
   chmod +x task-cli
   ```

## Usage

### Add a Task

```bash
task-cli add "Task description"
```

Output:

```
Task added successfully (ID: 1)
```

### Update a Task

```bash
task-cli update <task-id> "Updated task description"
```

Output:

```
Task updated successfully
```

### Delete a Task

```bash
task-cli delete <task-id>
```

Output:

```
Task deleted successfully
```

### Mark a Task as In Progress

```bash
task-cli mark-in-progress <task-id>
```

Output:

```
Task marked as in-progress
```

### Mark a Task as Done

```bash
task-cli mark-done <task-id>
```

Output:

```
Task marked as done
```

### List All Tasks

```bash
task-cli list
```

Output:

```
ID: 1 | Description: Buy groceries | Status: todo | Created At: <timestamp> | Updated At: <timestamp>
ID: 2 | Description: Cook dinner | Status: done | Created At: <timestamp> | Updated At: <timestamp>
```

### List Tasks by Status

#### List Tasks Not Done (To Do):

```bash
task-cli list todo
```

#### List Tasks In Progress:

```bash
task-cli list in-progress
```

#### List Tasks Done:

```bash
task-cli list done
```

## JSON Storage

The application uses a JSON file to store tasks. The JSON file is automatically created in the current directory if it does not already exist. All task operations read from and write to this file, ensuring data persistence.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## Contact

If you have any questions or suggestions, feel free to reach out at [47thommy@gmail.com].
