import argparse
from models import Task

def main():
    parser = argparse.ArgumentParser(description="Manage your task")
    subparser = parser.add_subparsers()

    # exclusive group of arguments
    task_parser = parser.add_mutually_exclusive_group()

    # new task argument
    task_parser.add_argument(
        "-n", "--new", 
        dest="new_task", 
        help="new task", 
        action="store", 
        default=argparse.SUPPRESS)

    # kill task argument
    task_parser.add_argument(
        "-k", "--kill", 
        help="kill a task",
        dest="kill_task",
        action="store",
        default=argparse.SUPPRESS)

    # Subparser show all task
    subparser_show = subparser.add_parser(
        "show", 
        help="Show all the task running")
    subparser_show.add_argument(
        "-a", "--active", 
        action="store_true", 
        dest="show_active")
    subparser_show.add_argument(
        "--all",
        action="store_true",
        dest="show_all")

    args = parser.parse_args()
    if "new_task" in args:
        Task.new(args.new_task)

    if "kill_task" in args:
        Task.kill(args.kill_task)

    if "show_active" in args:
        if args.show_active:
            active_tasks = Task.get_active()
            for task in active_tasks:
                task_str = "[{}] {} | {}".format(
                    task["relative_id"],
                    task["description"],
                    task["duration"])
                print(task_str)
    
    if "show_all" in args:
        if args.show_all:
            all_tasks = Task.get_all()
            for task in all_tasks:
                print(task)

if __name__ == "__main__":
    main()
