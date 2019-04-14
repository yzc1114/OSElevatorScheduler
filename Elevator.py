from PyQt5.QtCore import QBasicTimer, QTimer
from time import sleep
from functools import wraps
from PyQt5.QtCore import QThread, QMutex, pyqtSignal

class Elevator(object):
    """
    summary

    Attributes:
    current_level: an integer represent the level it stays
    current_target: an integer? represent the level it prepares to go
    targets: an array represent the remaining targets to go
    running_speed: an integer represent levels it goes per second
    is_running: a boolean indicating whether it is running or not
    is_door_opened: a boolean indicating whether the door is opened
    is_alarming: a boolean indicating whether the alarm is raised
    available_for_scheduler: a boolean indicating whether this elevator is available for a new run-task from level
    """
    door_open_trigger = None
    door_close_trigger = None
    current_level_trigger = None

    def __init__(self, running_speed, name, door_open_trigger, door_close_trigger, current_level_trigger, mutex):
        super(Elevator, self).__init__()
        self.name = None
        self.current_level = 1
        self.current_target = None
        self.targets = []
        self.running_speed = 1
        self.is_running = False
        self.is_door_opened = False
        self.is_alarming = False
        self.door_open_trigger = door_open_trigger
        self.door_close_trigger = door_close_trigger
        self.current_level_trigger = current_level_trigger
        self.lock = mutex
        #self.door_close_timer = None
        #self.door_close_timer = QTimer()
        #self.door_close_timer.timeout.connect(self.close_door)

        self.running_speed = running_speed
        self.name = name
        print(self.name + " is initialized")

    def alarm(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.is_alarming:
                print(self.name + "is raising alarm, so it cannot do anything")
            else:
                func(self, *args, **kwargs)
        return wrapper

    @alarm
    def run_to_level(self, level):
        """
        this elevator will run to level
        :param level: an integer represent the level this elevator goes to
        :return: void
        """
        assert self.is_running is False
        print(self.name + " start running to level " + str(level))
        self.current_target = level
        self.is_running = True
        # we use sleep to simulate running
        while self.current_target != self.current_level:
            # we use this lock to wait for the current level updating
            up = self.current_level < level
            if up:
                self.current_level += 1
                sleep(self.running_speed)
            else:
                self.current_level -= 1
                sleep(self.running_speed)
            # check the alarm
            # if it is alarming, then shut down
            self.current_level_trigger.emit(self.name + " " + str(self.current_level))
            print(self.name + " is currently at " + str(self.current_level) + " level")
            if self.is_alarming:
                return
            # we use this lock to wait for the current level updating
            self.lock.lock()
            self.lock.unlock()

        # running is over
        self.is_running = False
        self.current_target = None
        self.open_door()

    @alarm
    def open_door(self):
        print(self.name + " is opened")
        self.is_door_opened = True
        self.door_open_trigger.emit(self.name + " open signal received")
        #if self.door_close_timer:
        #    self.door_close_timer.stop()
        #self.door_close_timer = QBasicTimer()
        #self.door_close_timer.timeout.connect(self.close_door)
        #self.door_close_timer.start(3000)

    @alarm
    def close_door(self):
        print(self.name + " is closed")
        self.is_door_opened = False
        self.door_close_trigger.emit(self.name + " close signal received")
        #self.door_close_timer.stop()

    @alarm
    def raise_alarm(self):
        print(self.name + " is raising alarm")
        self.is_alarming = True

