from gui import *
from PyQt5.QtWidgets import QWidget
import sys
from Elevator_Scheduler import *
from PyQt5.QtCore import QTimer



class Form(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        Ui_Form.__init__(self)
        self.setupUi(self)
        self.init_buttons()
        self.t = ElevatorScheduler(max_level=20, num_elevators=5)
        self.t.start()
        for e_thread in self.t.elevator_threads:
            e_thread.door_open_trigger.connect(self.door_open_receiver)
            e_thread.door_close_trigger.connect(self.door_close_receiver)
            e_thread.current_level_trigger.connect(self.current_level_receiver)
        self.timers = [QTimer() for i in range(5)]
        self.timers[0].timeout.connect(self.timeout_e1_door_should_close)
        self.timers[1].timeout.connect(self.timeout_e2_door_should_close)
        self.timers[2].timeout.connect(self.timeout_e3_door_should_close)
        self.timers[3].timeout.connect(self.timeout_e4_door_should_close)
        self.timers[4].timeout.connect(self.timeout_e5_door_should_close)


    def init_buttons(self):
        for b in self.e1_buttons:
            b.clicked.connect(self.inside_elevator_button_clicked)
        for b in self.e2_buttons:
            b.clicked.connect(self.inside_elevator_button_clicked)
        for b in self.e3_buttons:
            b.clicked.connect(self.inside_elevator_button_clicked)
        for b in self.e4_buttons:
            b.clicked.connect(self.inside_elevator_button_clicked)
        for b in self.e5_buttons:
            b.clicked.connect(self.inside_elevator_button_clicked)

        self.e1_close.clicked.connect(self.close_door_button_clicked)
        self.e2_close.clicked.connect(self.close_door_button_clicked)
        self.e3_close.clicked.connect(self.close_door_button_clicked)
        self.e4_close.clicked.connect(self.close_door_button_clicked)
        self.e5_close.clicked.connect(self.close_door_button_clicked)

        self.e1_open.clicked.connect(self.open_door_button_clicked)
        self.e2_open.clicked.connect(self.open_door_button_clicked)
        self.e3_open.clicked.connect(self.open_door_button_clicked)
        self.e4_open.clicked.connect(self.open_door_button_clicked)
        self.e5_open.clicked.connect(self.open_door_button_clicked)

        self.e1_up.clicked.connect(self.up_button_clicked)
        self.e2_up.clicked.connect(self.up_button_clicked)
        self.e3_up.clicked.connect(self.up_button_clicked)
        self.e4_up.clicked.connect(self.up_button_clicked)
        self.e5_up.clicked.connect(self.up_button_clicked)

        self.e1_down.clicked.connect(self.down_button_button_clicked)
        self.e2_down.clicked.connect(self.down_button_button_clicked)
        self.e3_down.clicked.connect(self.down_button_button_clicked)
        self.e4_down.clicked.connect(self.down_button_button_clicked)
        self.e5_down.clicked.connect(self.down_button_button_clicked)

    def inside_elevator_button_clicked(self):
        sender = self.sender()
        name = sender.objectName()
        print("点击了", name)
        elevator_id = int(name[1])
        target_level = int(name.split('_')[-1])
        task = Task(task_run_from_elevator, target_level=target_level, elevator_id=elevator_id)
        self.t.add_task(task)

    def close_door_button_clicked(self):
        sender = self.sender()
        name = sender.objectName()
        print("点击了", name)
        elevator_id = int(name[1])
        self.timers[elevator_id-1].stop()
        task = Task(task_close, elevator_id=elevator_id)
        self.t.add_task(task)

    def open_door_button_clicked(self):
        sender = self.sender()
        name = sender.objectName()
        print("点击了", name)
        elevator_id = int(name[1])
        task = Task(task_open, elevator_id=elevator_id)
        self.t.add_task(task)

    def up_button_clicked(self):
        sender = self.sender()
        name = sender.objectName()
        print("点击了", name)
        elevator_id = int(name[1])
        target_level = None
        if elevator_id == 1:
            target_level = self.e1_spin_box.value()
        if elevator_id == 2:
            target_level = self.e2_spin_box.value()
        if elevator_id == 3:
            target_level = self.e3_spin_box.value()
        if elevator_id == 4:
            target_level = self.e4_spin_box.value()
        if elevator_id == 5:
            target_level = self.e5_spin_box.value()
        print(target_level)
        task = Task(task_run_from_level, target_level=int(target_level), elevator_id=elevator_id)
        self.t.add_task(task)

    def down_button_button_clicked(self):
        sender = self.sender()
        name = sender.objectName()
        print("点击了", name)
        elevator_id = int(name[1])
        target_level = None
        if elevator_id == 1:
            target_level = self.e1_spin_box.value()
        if elevator_id == 2:
            target_level = self.e2_spin_box.value()
        if elevator_id == 3:
            target_level = self.e3_spin_box.value()
        if elevator_id == 4:
            target_level = self.e4_spin_box.value()
        if elevator_id == 5:
            target_level = self.e5_spin_box.value()
        task = Task(task_run_from_level, target_level=int(target_level), elevator_id=elevator_id)
        self.t.add_task(task)

    def door_open_receiver(self, info):
        print(info)
        elevator_name = info.split(" ")[0]
        elevator_id = int(elevator_name[-1])
        self.timers[elevator_id-1].start(3000)
        # refresh ui
        if elevator_id == 1:
            self.e_door_1.setText("门状态：开")
        if elevator_id == 2:
            self.e_door_2.setText("门状态：开")
        if elevator_id == 3:
            self.e_door_3.setText("门状态：开")
        if elevator_id == 4:
            self.e_door_4.setText("门状态：开")
        if elevator_id == 5:
            self.e_door_5.setText("门状态：开")

    def door_close_receiver(self, info):
        print(info)
        # refresh ui
        elevator_name = info.split(" ")[0]
        elevator_id = int(elevator_name[-1])
        # refresh ui
        if elevator_id == 1:
            self.e_door_1.setText("门状态：关")
        if elevator_id == 2:
            self.e_door_2.setText("门状态：关")
        if elevator_id == 3:
            self.e_door_3.setText("门状态：关")
        if elevator_id == 4:
            self.e_door_4.setText("门状态：关")
        if elevator_id == 5:
            self.e_door_5.setText("门状态：关")

    def timeout_e1_door_should_close(self):
        print("e1到时!!!!")
        self.close_timer(0)

    def timeout_e2_door_should_close(self):
        print("e2到时!!!!")
        self.close_timer(1)

    def timeout_e3_door_should_close(self):
        print("e3到时!!!!")
        self.close_timer(2)

    def timeout_e4_door_should_close(self):
        print("e4到时!!!!")
        self.close_timer(3)

    def timeout_e5_door_should_close(self):
        print("e5到时!!!!")
        self.close_timer(4)

    def close_timer(self, timer_id):
        self.timers[timer_id].stop()
        self.t.elevator_threads[timer_id].elevator.close_door()


    def current_level_receiver(self, info):
        print("receiver ---> " + info)
        elevator_name, current_level = info.split(" ")
        elevator_id = int(elevator_name[-1])
        # refresh ui
        if elevator_id == 1:
            self.level_1.setText(current_level + " 层")
            self.e_slider_1.setValue(int(current_level))
        if elevator_id == 2:
            self.level_2.setText(current_level + " 层")
            self.e_slider_2.setValue(int(current_level))
        if elevator_id == 3:
            self.level_3.setText(current_level + " 层")
            self.e_slider_3.setValue(int(current_level))
        if elevator_id == 4:
            self.level_4.setText(current_level + " 层")
            self.e_slider_4.setValue(int(current_level))
        if elevator_id == 5:
            self.level_5.setText(current_level + " 层")
            self.e_slider_5.setValue(int(current_level))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())
