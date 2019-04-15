from Elevator_Scheduler import *

scheduler = ElevatorScheduler(num_elevators=5, max_level=20)
check_status = "check_status"
task_types = [task_run_from_level, task_run_from_elevator, task_open, task_close, task_alarm, check_status]


if __name__ == "__main__":

    def get_elevator_id(tip):
        while True:
            elevator_id_in = int(input(tip))
            if elevator_id_in <= 0 or elevator_id_in > 5:
                print("wrong, try again")
            else:
                break
        return elevator_id_in

    def get_level(tip):
        while True:
            level_in = int(input(tip))
            if level_in <= 0 or level_in > 20:
                print("wrong, try again")
            else:
                break
        return level_in


    print("This building has 20 levels, and 5 elevators in total")
    scheduler.start()


    while True:
        print("create a new order ---")
        task_type = ""
        while True:
            print("order types --> ", task_types)
            task_type = input("enter your order type :")
            if task_type in task_types:
                break
            else:
                print("this type is not existed, please enter again")

        if task_type == task_run_from_level:
            level = get_level("enter your current level: ")
            task = Task(task_type, target_level=level, elevator_id=None)
            print("order is built")
            scheduler.add_task(task)

        if task_type == task_run_from_elevator:
            level = get_level("enter your target level: ")
            elevator_id = get_elevator_id("enter your elevator id: ")
            task = Task(task_type, target_level=level, elevator_id=elevator_id-1)
            print("order is built")
            scheduler.add_task(task)

        if task_type == task_open or task_type == task_close or task_type == task_alarm:
            elevator_id = get_elevator_id("enter the your current elevator: ")
            task = Task(task_type, target_level=None, elevator_id=elevator_id-1)
            print("order is built")
            scheduler.add_task(task)

        if task_type == check_status:
            scheduler.print_status()
