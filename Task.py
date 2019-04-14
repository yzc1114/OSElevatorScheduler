from time import time

task_run_from_level = "new_run_from_level"
task_run_from_elevator = "new_run_from_elevator"
task_open = "open"
task_close = "close"
task_alarm = "alarm"


class Task(object):
    """
    this class describe a task made by user

    Attributes:
    task_type: str
    target_floor: integer
        when task_type is run_from_elevator, this variable represent the determination
        when task_type is run_from_level, this variable represent the calling level
    elevator_id: integer
    """

    def __init__(self, task_type, target_level=None, elevator_id=None):
        self.task_type = task_type
        self.target_level = target_level
        self.elevator_id = elevator_id - 1
        self.task_create_time = int(round(time() * 1000))
        if task_type == task_run_from_elevator:
            assert target_level is not None and elevator_id is not None
        if task_type == task_open or task_type == task_close or task_type == task_alarm:
            assert elevator_id is not None
