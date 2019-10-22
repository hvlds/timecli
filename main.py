import argparse

parser = argparse.ArgumentParser(description="Manage your task")
subparser = parser.add_subparsers()

# Subparsers task
subparser_task = subparser.add_parser("task", help="Add a new task")
subparser_task.add_argument("-n", "--new", action="store", dest="new_task", 
                    help="description of task")

# Subparser list all task
subparser_task_list = subparser.add_parser("list", help="Show all the task running")
subparser_task_list.add_argument("-s", "--show")

args = parser.parse_args()
print(args.new_task)