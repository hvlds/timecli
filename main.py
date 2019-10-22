import argparse

parser = argparse.ArgumentParser(description="Manage your task")
parser.add_argument("-t", "--task", dest="task", required=True,
                    help="description of task")

args = parser.parse_args()
print(args.task)