class Task:
    def __init__(self, name, arrival_time, estimated_time, urgency_level):
        self.name = name
        self.arrival_time = arrival_time
        self.estimated_time = estimated_time
        self.urgency_level = urgency_level

# Sample tasks
tasks = [
    Task("PatientA", 0, 30, 3),
    Task("PatientB", 10, 20, 5),
    Task("PatientC", 15, 40, 2),
    Task("PatientD", 20, 15, 4),
]

def fcfs_scheduling(tasks):
    schedule = []
    current_time = 0
    waiting_time = 0
    turnaround_time = 0

    for task in tasks:
        if task.arrival_time > current_time:
            current_time = task.arrival_time
        schedule.append((task.name, current_time))
        waiting_time += current_time - task.arrival_time
        current_time += task.estimated_time
        turnaround_time += current_time - task.arrival_time

    average_waiting_time = waiting_time / len(tasks)
    average_turnaround_time = turnaround_time / len(tasks)

    return schedule, average_waiting_time, average_turnaround_time

def sjf_scheduling(tasks):
    tasks_copy = tasks.copy()  # Create a copy of the tasks to preserve the original list
    tasks_copy.sort(key=lambda x: (x.arrival_time, x.estimated_time))
    schedule = []
    current_time = 0
    waiting_time = 0
    turnaround_time = 0

    while tasks_copy:
        eligible_tasks = [task for task in tasks_copy if task.arrival_time <= current_time]
        if not eligible_tasks:
            current_time += 1
            continue

        shortest_task = min(eligible_tasks, key=lambda x: x.estimated_time)
        schedule.append((shortest_task.name, current_time))
        waiting_time += current_time - shortest_task.arrival_time
        current_time += shortest_task.estimated_time
        turnaround_time += current_time - shortest_task.arrival_time
        tasks_copy.remove(shortest_task)

    # Calculate average waiting and turnaround times
    average_waiting_time = waiting_time / len(schedule)
    average_turnaround_time = turnaround_time / len(schedule)

    # Return the scheduling results
    return schedule, average_waiting_time, average_turnaround_time

def ps_scheduling(tasks):
    tasks_copy = tasks.copy()  # Create a copy of the tasks to preserve the original list
    tasks_copy.sort(key=lambda x: (x.arrival_time, x.estimated_time))
    schedule = []
    current_time = 0
    waiting_time = 0
    turnaround_time = 0

    while tasks_copy:
        eligible_tasks = [task for task in tasks_copy if task.arrival_time <= current_time]
        if not eligible_tasks:
            current_time += 1
            continue

        highest_priority_task = min(eligible_tasks, key=lambda x: x.estimated_time)
        schedule.append((highest_priority_task.name, current_time))
        waiting_time += current_time - highest_priority_task.arrival_time
        current_time += highest_priority_task.estimated_time
        turnaround_time += current_time - highest_priority_task.arrival_time
        tasks_copy.remove(highest_priority_task)

    # Calculate average waiting and turnaround times
    average_waiting_time = waiting_time / len(schedule)
    average_turnaround_time = turnaround_time / len(schedule)

    # Return the scheduling results
    return schedule, average_waiting_time, average_turnaround_time

def rr_scheduling(tasks, time_quantum):
    tasks_copy = tasks.copy()  # Create a copy of the tasks to preserve the original list
    tasks_copy.sort(key=lambda x: x.arrival_time)
    schedule = []
    current_time = 0
    waiting_time = 0
    turnaround_time = 0

    while tasks_copy:
        task = tasks_copy.pop(0)
        if current_time < task.arrival_time:
            current_time = task.arrival_time
        schedule.append((task.name, current_time))
        waiting_time += current_time - task.arrival_time

        if task.estimated_time <= time_quantum:
            current_time += task.estimated_time
            turnaround_time += current_time - task.arrival_time
        else:
            # Create a new task with remaining time
            remaining_time = task.estimated_time - time_quantum
            new_task = Task(task.name, current_time, remaining_time, task.urgency_level)
            tasks_copy.append(new_task)
            current_time += time_quantum

    # Calculate average waiting and turnaround times
    average_waiting_time = waiting_time / len(schedule)
    average_turnaround_time = turnaround_time / len(schedule)

    # Return the scheduling results
    return schedule, average_waiting_time, average_turnaround_time

time_quantum = 2

# Run and print all scheduling algorithms
fcfs_schedule, fcfs_avg_waiting_time, fcfs_avg_turnaround_time = fcfs_scheduling(tasks)
sjf_schedule, sjf_avg_waiting_time, sjf_avg_turnaround_time = sjf_scheduling(tasks)
ps_schedule, ps_avg_waiting_time, ps_avg_turnaround_time = ps_scheduling(tasks)
rr_schedule, rr_avg_waiting_time, rr_avg_turnaround_time = rr_scheduling(tasks, time_quantum)

print("FCFS Schedule:")
for task, start_time in fcfs_schedule:
    print(f"{task}: Start Time = {start_time}")
print(f"Average Waiting Time: {fcfs_avg_waiting_time}")
print(f"Average Turnaround Time: {fcfs_avg_turnaround_time}")

print("\nSJF Schedule:")
for task, start_time in sjf_schedule:
    print(f"{task}: Start Time = {start_time}")
print(f"Average Waiting Time: {sjf_avg_waiting_time}")
print(f"Average Turnaround Time: {sjf_avg_turnaround_time}")

print("\nPriority Schedule:")
for task, start_time in ps_schedule:
    print(f"{task}: Start Time = {start_time}")
print(f"Average Waiting Time: {ps_avg_waiting_time}")
print(f"Average Turnaround Time: {ps_avg_turnaround_time}")

print("\nRound Robin Schedule:")
for task, start_time in rr_schedule:
    print(f"{task}: Start Time = {start_time}")
print(f"Average Waiting Time: {rr_avg_waiting_time}")
print(f"Average Turnaround Time: {rr_avg_turnaround_time}")

# Compare scheduling algorithms
average_waiting_times = {
    "FCFS": fcfs_avg_waiting_time,
    "SJF": sjf_avg_waiting_time,
    "Priority": ps_avg_waiting_time,
    "Round Robin": rr_avg_waiting_time,
}

average_turnaround_times = {
    "FCFS": fcfs_avg_turnaround_time,
    "SJF": sjf_avg_turnaround_time,
    "Priority": ps_avg_turnaround_time,
    "Round Robin": rr_avg_turnaround_time,
}

most_efficient_algorithm = min(average_waiting_times, key=average_waiting_times.get)
most_fair_algorithm = min(average_turnaround_times, key=average_turnaround_times.get)

print("\nMost Efficient Scheduling Algorithm:", most_efficient_algorithm)
print("Most Fair Scheduling Algorithm:", most_fair_algorithm)