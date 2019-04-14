from PyQt5.QtCore import QThread
from Elevator_Scheduler import *

class QThread_Wrapper(QThread):
    def __init__(self, *args, **kwargs):
        super(QThread_Wrapper, self).__init__(*args, **kwargs)
        self.scheduler = ElevatorScheduler(max_level=20, num_elevators=5)

    def run(self):
        self.scheduler.start()