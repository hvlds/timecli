import argparse
from models import Task

def main():
    parser = argparse.ArgumentParser(description="Manage your task")
    subparser = parser.add_subparsers()

    # Subparsers task
    subparser_task = subparser.add_parser(
        "task", 
        help="Add a new task")

    # new task argument
    subparser_task.add_argument(
        "-n", "-new", 
        dest="new_task", 
        help="new task", 
        action="store", 
        default=argparse.SUPPRESS)

    # kill task argument
    subparser_task.add_argument(
        "-k", "-kill", 
        help="kill a task",
        dest="kill_task",
        action="store",
        default=argparse.SUPPRESS)

    # Subparser list all task
    subparser_task_list = subparser.add_parser("list", help="Show all the task running")
    subparser_task_list.add_argument(
        "-s", "-show", 
        action="store_true", 
        dest="show")

    args = parser.parse_args()
    if "new_task" in args:
        Task.new(args.new_task)
        print(args.new_task)

    if "kill_task" in args:
        Task.kill(args.kill_task)

    if "show" in args:
        active_tasks = Task.get_active_tasks()
        for task in active_tasks:
            task_str = "[{}] {} | {}".format(
                task["relative_id"],
                task["description"],
                task["duration"]
            )
            print(task_str)

if __name__ == "__main__":
    main()
