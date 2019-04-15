# 电梯调度算法

### 使用语言
 1. python 3.6.6

### 使用第三方库
 1. PyQt5
 2. PyQt designer

### 最终实现截图
![最终实现截图1](/images/show.png)


### 使用说明
**环境需要使用venv文件夹中的虚拟环境运行，以start_gui.py为主文件运行**

**注意
每个滑块代表一个电梯，每个电梯的左侧的20个按钮代表了电梯内部的20个按钮，按下之后，电梯就会到达相应楼层，
每个电梯的上面的标签代表它所在的楼层，它下面的按钮：上、下，以及左侧的数字输入选框，这几个部分的功能代表：
数字代表楼层，上和下按钮代表该层的向上，向下按钮。 再下面的开、关即代表电梯内部的开关按钮。 最下方的标签
代表了电梯门的开关状态。**

### 参数选择
本次实现中，我们的楼层高度为20层，一共5个电梯，电梯的速度为1层/秒，电梯门的保持开启的时间为3秒。

### 算法简介
1. 在楼层中按电梯时--算法思路
   - 对于电梯调度算法来讲，我们有从某个楼层按上或下，以及在电梯内按下某层楼，以及按开关门等操作。
   - 我们的算法主要运用了最短任务用时算法调度的思想，我们需要在新的命令来临时，找到执行这个命令
   - 用时最短的那个电梯。
   - 例子： 比如说，四个电梯均在1楼，只有一个电梯在从10楼往下运行，此时一个人在6楼按下了上，我们
   - 算法应该会计算出最合适的那个电梯来接6楼这个人，所以我们计算出每个电梯离6楼的距离，发现只有从
   - 十楼往下运行的电梯离他最近，所以应当由这个电梯来接它。
   - 但是，问题如果变一下，加入这个电梯当时在10楼向上运行，那么我们就不应该让这个电梯再去6楼接这个
   - 人，因为它还需要向上走一阵子，而还需走多远，以及它后面的运行轨迹是不可预测的，所以我们从在1楼
   - 停着的4个电梯中挑选一个，来接6楼的人。
   - 所以我们的算法核心思想是，检测出到达接送楼层用时最短，且运行方向不冲突的那个电梯，就是我们想要
   - 电梯
2. 在电梯中按电梯时--算法思路
   - 在电梯中按电梯时有一些东西要考虑到，比如说，在我们按下了20楼之后，我们的电梯开始向20楼进发，但是
   - 如果我们在运行到10楼的时候，又按下了5楼和15楼，我们的电梯应该能够做到，在15楼停下，再向20楼进发，
   - 再向5楼运行，我们的算法原则，是————永不回头，就近原则。永不回头的意思是说，在面对的方向中，还有某
   - 个按钮对应的楼层还没有到达过，我们就需要前往它，而在反方向的，我们一概不去考虑这件事情。而对于
   - 就近原则，这个的意思是我们在同一方向上的可停楼层，我们永远选择离得最近的先到达，这样就保证了
   - 时间不会浪费

### 算法核心代码
1. 在楼层中按电梯时--算法
```
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
                continue
            proper_elevator_thread = self.elevator_threads[proper_elevator_thread_index]
            # we simply transform the task into a task from elevator in which case it will simplify the schedule job
            task.task_type = task_run_from_elevator
            task.elevator_id = int(proper_elevator_thread.elevator.name[-1])-1
            self.add_task(task)
```
```
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
            # but if the new task is in between the current_level and current_target,
            # we have more options
            e_thread = self.elevator_threads[task.elevator_id]
            e_thread.lock.lock()
            if e_thread.elevator.is_running:
                # here we find the next most proper level to go
                # as time goes by, there maybe new targets being added,
                # so we need this lock,
                # rule: Never Change Direction, Always Choose The Closed One
                current_target = e_thread.elevator.current_target
                current_level = e_thread.elevator.current_level
                new_target_level = task.target_level
                e_thread.elevator.targets.append(new_target_level)
                e_thread.elevator.targets.append(current_target)
                targets = e_thread.elevator.targets.copy()
                is_up = current_target > current_level
                if is_up:
                    # we need the bigger slice to be executed first,
                    # because we are uping
                    smaller_slice = [x for x in targets if x < current_level]
                    bigger_slice = [x for x in targets if x >= current_level]
                    smaller_slice.sort()
                    smaller_slice.reverse()
                    bigger_slice.sort()
                    new_targets = bigger_slice + smaller_slice
                    e_thread.elevator.targets = new_targets
                    e_thread.elevator.current_target = e_thread.elevator.targets.pop(0)
                else:
                    # we need the smaller slice to be executed first in this case
                    smaller_slice = [x for x in targets if x < current_level]
                    bigger_slice = [x for x in targets if x >= current_level]
                    smaller_slice.sort()
                    smaller_slice.reverse()
                    bigger_slice.sort()
                    new_targets = smaller_slice + bigger_slice
                    e_thread.elevator.targets = new_targets
                    e_thread.elevator.current_target = e_thread.elevator.targets.pop(0)
                e_thread.lock.unlock()
                return
            else:
                e_thread.elevator.targets.append(task.target_level)
                e_thread.lock.unlock()
                return
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
```

