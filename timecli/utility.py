from .models import Task
from .color import Color


def list_running_tasks():
    running_tasks = Task.get_running()
    color = Color()
    title = color.text_bold("Task running", underline=True)
    print(title)
    for task in running_tasks:
            relative_id = "[{}] ".format(
                task["relative_id"],
            )
            description = "{: <20}".format(
                task["description"]
            )
            duration = "\tRunning time: {: <20}".format(
                task["duration"]
            )
            task_str = color.text_color(relative_id, "yellow")
            task_str += description
            task_str += color.text_color(duration, "cyan")
            print(task_str)
