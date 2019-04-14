from threading import Thread, ThreadError, current_thread, Lock
from PyQt5.QtCore import QThread, QBasicTimer, QMutex
from Elevator_Thread import ElevatorThread
from Task import *
from time import sleep








class ElevatorScheduler(QThread):
    """
    this class contains the scheduler algorithm

    Attributes:
    max_level: an integer represent the maximum of the building
    elevator_threads: an array stores all the ElevatorThread
    num_elevators: an integer represent the num of elevators
    waiting_tasks: an array stores all the tasks waiting to be executed
    """

    def __init__(self, max_level, num_elevators, *args, **kwargs):
        super(ElevatorScheduler, self).__init__(*args, **kwargs)
        self.max_level = max_level
        self.num_elevators = num_elevators
        self.elevator_threads = []
        self.lock = QMutex()
        self.waiting_tasks = []

        for i in range(num_elevators):
            self.elevator_threads.append(ElevatorThread(elevator_name="elevator_" + str(i+1),
                                                        running_speed=1))

        #self.schedule_thread = QThread()
        #self.schedule_thread = Thread(target=self.schedule_waiting_tasks)

        print("elevators and scheduler are all initialized")

    def run(self):
        self.lets_start()

    def lets_start(self):
        print("scheduler is started")
        for i in range(self.num_elevators):
            self.elevator_threads[i].start()
        self.schedule_waiting_tasks()


    def add_task(self, task):
        """
        add the task into the corresponding elevator thread
        :param task: an object of Task
        :return: void
        """
        print("scheduler received new task -->" + task.task_type)
        if task.task_type == task_run_from_level:
            # if the task type is a call from level,
            # it has to be waiting until there is an available elevator
            self.lock.lock()
            self.waiting_tasks.append(task)
            self.lock.unlock()
        elif task.task_type == task_run_from_elevator:
            # if the task type is a call from elevator
            # we simply add the new target into the elevator targets(array)
            e_thread = self.elevator_threads[task.elevator_id]
            e_thread.lock.lock()
            e_thread.elevator.targets.append(task.target_level)
            e_thread.lock.unlock()
        elif task.task_type == task_alarm:
            # if alarm
            # we simply call the alarm function
            # because in the running function, we check the alarm whenever
            # we reach a new level
            e_thread = self.elevator_threads[task.elevator_id]
            e_thread.lock.lock()
            e_thread.elevator.raise_alarm()
            e_thread.lock.unlock()
            pass
        else:
            self.execute_door_task(task)

    def execute_door_task(self, task):
        """
        execute the door_task which can be instantly executed
        this door_task can only be executed when the door is opened
        in other word, when the elevator is running, this task cannot
        be executed
        :param task: Task object
        :return: void
        """
        print("executing instant task " + task.task_type + " from elevator_" + str(task.elevator_id+1))

        e_thread = self.elevator_threads[task.elevator_id]
        if e_thread.elevator.is_running is False:
            e_thread.lock.lock()
            e_thread.door_tasks.append(task)
            e_thread.lock.unlock()
        else:
            print("since the elevator is running, this task cannot be executed")

    def schedule_waiting_tasks(self):
        """
        this is a independent thread function
        in this function, we schedule all the run_from_level tasks
        find a proper elevator to take that task
        and loop all the way
        :param task: a Task object
        :return: void
        """
        while True:
            if len(self.waiting_tasks) == 0:
                sleep(0)
                continue
            # since we find the proper thread of elevator
            # we decide which task need to be execute first
            # rule : we select the task which has the longest waiting time
            self.lock.lock()
            task = self.waiting_tasks.pop(0)
            self.lock.unlock()

            proper_elevator_thread_index = None
            min_distance = 1000
            for i, elevator_thread in enumerate(self.elevator_threads):
                if elevator_thread.elevator.is_alarming is False:
                    if min_distance > abs(elevator_thread.elevator.current_level - task.target_level):
                        if self.elevator_threads[i].elevator.is_running:
                            # if the direction is the same, we choose this elevator
                            target_level = self.elevator_threads[i].elevator.current_target
                            current_level = self.elevator_threads[i].elevator.current_level
                            new_target_level = task.target_level
                            is_uping = target_level > current_level
                            if is_uping is True and new_target_level >= current_level:
                                # in this case, we can choose
                                pass
                            elif is_uping is True and new_target_level < current_level:
                                # in this case, we cannot choose
                                continue
                            elif is_uping is False and new_target_level <= current_level:
                                # in this case, we can choose
                                pass
                            else:
                                # in this case, we cannot choose
                                continue

                        min_distance = abs(elevator_thread.elevator.current_level - task.target_level)
                        proper_elevator_thread_index = i
            if proper_elevator_thread_index is None:
                print("we have no elevator available anymore")
                exit(-1)
            proper_elevator_thread = self.elevator_threads[proper_elevator_thread_index]
            # we add the task.target_level into the targets array
            # so that, it is equal to we push a button in the elevator
            # this will simplify the schedule, hand over some tasks to
            # that elevator
            proper_elevator_thread.lock.lock()
            proper_elevator_thread.elevator.targets.append(task.target_level)
            proper_elevator_thread.lock.unlock()

    def print_status(self):
        for i in range(self.num_elevators):
            e_thread = self.elevator_threads[i]
            print(e_thread.elevator.name + " is currently at " + str(e_thread.elevator.current_level) + " level")



