import argparse
from models import Task
from color import Color

def main():
    # Initialize the color changer class
    color = Color()

    # Define main CLI Parsers
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
        default=argparse.SUPPRESS
    )

    # kill task argument
    task_parser.add_argument(
        "-k", "--kill",
        help="kill a task",
        dest="kill_task",
        action="store",
        default=argparse.SUPPRESS
    )
    
    # kill last task argument
    task_parser.add_argument(
        "--kill-last",
        help="kill the last entered task",
        dest="kill_last_task",
        action="store_true",
        default=argparse.SUPPRESS
    )

    # Subparser show all task
    subparser_show = subparser.add_parser(
        "show",
        help="Show all the task running"
    )
    subparser_show.add_argument(
        "-r", "--running", 
        action="store_true", 
        dest="show_running"
    )
    subparser_show.add_argument(
        "-a",
        "--all",
        action="store_true",
        dest="show_all"
    )

    args = parser.parse_args()
    if "new_task" in args:
        Task.new(args.new_task)

    if "kill_task" in args:
        Task.kill(args.kill_task)
    
    if "kill_last_task" in args:
        if args.kill_last_task:
            Task.kill_last()

    if "show_running" in args:
        if args.show_running:
            running_tasks = Task.get_running()
            for task in running_tasks:
                task_str = "[{}] {}".format(
                    task["relative_id"],
                    task["description"]
                )
                duration_text = " Running time: {}".format(
                    task["duration"]
                )
                task_str += color.text_color(duration_text, "cyan", bold=True)
                print(task_str)

    if "show_all" in args:
        if args.show_all:
            all_tasks = Task.get_all()
            for task in all_tasks:
                print(task)

if __name__ == "__main__":
    main()
