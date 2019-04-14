from threading import Thread, Lock, Timer
from Elevator import Elevator
from Task import *
from time import sleep
from PyQt5.QtCore import QThread, QMutex, pyqtSignal

class ElevatorThread(QThread):
    """
    this class is the thread for an elevator
    """
    door_open_trigger = pyqtSignal(str)
    door_close_trigger = pyqtSignal(str)
    current_level_trigger = pyqtSignal(str)

    def __init__(self, elevator_name, running_speed):
        super(ElevatorThread, self).__init__()
        self.door_tasks = []
        #self.lock = Lock()
        self.lock = QMutex()
        self.elevator = Elevator(running_speed=running_speed,
                                 name=elevator_name,
                                 door_close_trigger=self.door_close_trigger,
                                 door_open_trigger=self.door_open_trigger,
                                 current_level_trigger=self.current_level_trigger,
                                 mutex=self.lock)

    def run(self):
        """this method describe how every ElevatorThread is scheduled"""
        while True:
            if len(self.door_tasks) == 0 and len(self.elevator.targets) == 0:
                # when there is no task, we distribute the time slice to other threads
                sleep(0)
            while len(self.door_tasks) != 0 and self.elevator.is_running is False:
                # first execute all the instance tasks
                # while door is opening
                # since the door can only be opened or closed when the elevator is not running
                self.execute_door_task()
            if len(self.elevator.targets) != 0 and self.elevator.is_door_opened is False:
                # if we have buttons clicked in the elevator
                # we goes to the next proper level
                # find the proper level and go there

                # first we need to clear the door tasks
                self.door_tasks.clear()

                current_level = self.elevator.current_level
                min_distance = 1000
                proper_index = None
                if not self.lock.tryLock():
                    continue
                # the schedule work is done in big scheduler, so we only need to pop the first one


                ## here we find the next most proper level to go
                ## as time goes by, there maybe new targets being added,
                ## so we need this lock,
                ## rule: Never Change Direction, Always Choose The Closed One
                #for index, target in enumerate(self.elevator.targets):
                #    if abs(target - current_level) < min_distance:
                #        min_distance = abs(target - current_level)
                #        proper_index = index
                #proper_level = self.elevator.targets[proper_index]
                proper_level = self.elevator.targets.pop(0)
                self.lock.unlock()

                self.elevator.run_to_level(proper_level)
                pass

    def execute_door_task(self):
        # we need this lock because this array may be edited in the schedule thread
        self.lock.lock()
        task = self.door_tasks.pop(0)
        self.lock.unlock()
        if task.task_type == task_close:
            if self.elevator.is_door_opened:
                self.elevator.close_door()
            else:
                print("elevator_" + str(task.elevator_id+1) + "is already closed")
            return
        if task.task_type == task_open:
            self.elevator.open_door()
            return

        if task.task_type == task_alarm:
            self.elevator.alarm()
            return

        print("task is not well-built, please checked the code")