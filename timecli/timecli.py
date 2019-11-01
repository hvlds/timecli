import argparse
from .models import Task
from .color import Color
from .utility import list_running_tasks


class TaskCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Manage your task")
        self.subparser = self.parser.add_subparsers()

        # exclusive group of arguments
        task_parser = self.parser.add_mutually_exclusive_group()

        task_parser.add_argument(
            "-n",
            "--new",
            dest="new_task",
            help="new task",
            action="store",
            default=argparse.SUPPRESS
        )
        task_parser.add_argument(
            "-p",
            "--project",
            dest="project",
            help="Choose a project for the task",
            default=argparse.SUPPRESS
        )

        # Subparser kill task
        subparser_kill = self.subparser.add_parser(
            "kill",
            help="Kill (terminate) a running task"
        )
        kill_group = subparser_kill.add_mutually_exclusive_group()
        kill_group.add_argument(
            "kill_id",
            type=int,
            metavar="ID",
            help="ID (relative) of the task",
            action="store",
            nargs='*',
            default=argparse.SUPPRESS
        )
        kill_group.add_argument(
            "--last",
            help="kill the last entered task",
            dest="kill_last_task",
            action="store_true",
            default=argparse.SUPPRESS
        )

        # Subparser project
        subparser_project = self.subparser.add_parser(
            "project",
            help="Manage your projects"
        )
        subparser_project.add_argument(
            "-n",
            "--n",
            help="Create a new project",
            action="store",
        )

        # Subparser list all task
        subparser_list = self.subparser.add_parser(
            "list",
            help="list all the task running"
        )
        list_group = subparser_list.add_mutually_exclusive_group()
        list_group.add_argument(
            "-r", "--running",
            action="store_true",
            default=argparse.SUPPRESS,
            dest="list_running"
        )
        list_group.add_argument(
            "-a",
            "--all",
            action="store_true",
            default=argparse.SUPPRESS,
            dest="list_all",
        )
    
    def menu(self):
        args = self.parser.parse_args()
        if "new_task" in args:
            Task.new(args.new_task)

        elif "kill_last_task" in args:
            if args.kill_last_task:
                Task.kill_last()

        elif "kill_id" in args:
            Task.kill(args.kill_id[0])

        elif "list_running" in args:
            if args.list_running:
                list_running_tasks()

        elif "list_all" in args:
            if args.list_all:
                all_tasks = Task.get_all()
                for task in all_tasks:
                    print(task)

def main():
    taskcli = TaskCLI()
    taskcli.menu()
