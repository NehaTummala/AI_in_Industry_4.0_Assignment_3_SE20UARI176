class Process:
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0  # Initialize waiting time for each process
        self.turnaround_time = 0  # Initialize turnaround time for each process

# Define your list of processes here
processes = [
    Process("P1", 0, 24, 3),
    Process("P2", 4, 3, 1),
    Process("P3", 5, 3, 4),
    Process("P4", 6, 12, 2),
]

def fcfs_scheduling(processes):
    schedule = []  # Store the schedule of processes
    current_time = 0  # Initialize the current time

    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)

    for process in processes:
        # Calculate waiting time for the current process
        process.waiting_time = max(0, current_time - process.arrival_time)

        # Update the current time
        current_time += process.burst_time

        # Calculate turnaround time for the current process
        process.turnaround_time = process.waiting_time + process.burst_time

        # Append the process name and its start time to the schedule
        schedule.append((process.name, current_time - process.burst_time))

    # Calculate average waiting and turnaround times
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    average_waiting_time = total_waiting_time / len(processes)
    average_turnaround_time = total_turnaround_time / len(processes)


    return schedule, average_waiting_time, average_turnaround_time
# Function to perform SJF scheduling
def sjf_scheduling(processes):
    if not processes:
        return [], 0, 0

    schedule = []  # Store the schedule of processes
    current_time = 0  # Initialize the current time

    # Create a copy of processes to preserve the original list
    processes_copy = processes.copy()

    waiting_times = []  # List to store waiting times for each process
    turnaround_times = []  # List to store turnaround times for each process

    while processes_copy:
        eligible_processes = [process for process in processes_copy if process.arrival_time <= current_time]

        if not eligible_processes:
            # No eligible process, increment the current time
            current_time += 1
        else:
            # Find the process with the shortest burst time
            shortest_burst_process = min(eligible_processes, key=lambda x: x.burst_time)

            # Calculate waiting time for the current process
            waiting_time = max(0, current_time - shortest_burst_process.arrival_time)
            waiting_times.append(waiting_time)

            # Update the current time
            current_time += shortest_burst_process.burst_time

            # Calculate turnaround time for the current process
            turnaround_time = waiting_time + shortest_burst_process.burst_time
            turnaround_times.append(turnaround_time)

            # Append the process name and its start time to the schedule
            schedule.append((shortest_burst_process.name, current_time - shortest_burst_process.burst_time))

            # Remove the process from the list
            processes_copy.remove(shortest_burst_process)

    # Calculate average waiting and turnaround times
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times)

    return schedule, average_waiting_time, average_turnaround_time


# Function to perform Priority scheduling
def priority_scheduling(processes):
    if not processes:
        return [], 0, 0

    schedule = []  # Store the schedule of processes
    current_time = 0  # Initialize the current time

    # Create a copy of processes to preserve the original list
    processes_copy = processes.copy()

    waiting_times = []  # List to store waiting times for each process
    turnaround_times = []  # List to store turnaround times for each process

    while processes_copy:
        eligible_processes = [process for process in processes_copy if process.arrival_time <= current_time]

        if not eligible_processes:
            # No eligible process, increment the current time
            current_time += 1
        else:
            # Find the process with the highest priority
            highest_priority_process = min(eligible_processes, key=lambda x: x.priority)

            # Calculate waiting time for the current process
            waiting_time = max(0, current_time - highest_priority_process.arrival_time)
            waiting_times.append(waiting_time)

            # Update the current time
            current_time += highest_priority_process.burst_time

            # Calculate turnaround time for the current process
            turnaround_time = waiting_time + highest_priority_process.burst_time
            turnaround_times.append(turnaround_time)

            # Append the process name and its start time to the schedule
            schedule.append((highest_priority_process.name, current_time - highest_priority_process.burst_time))

            # Remove the process from the list
            processes_copy.remove(highest_priority_process)

    # Calculate average waiting and turnaround times
    average_waiting_time = sum(waiting_times) / len(waiting_times) if waiting_times else 0
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times) if turnaround_times else 0

    return schedule, average_waiting_time, average_turnaround_time

# Function to perform Round Robin scheduling with a time quantum of 4
def round_robin_scheduling(processes, time_quantum=4):
    if not processes:
        return [], 0, 0

    schedule = []  # Store the schedule of processes
    current_time = 0  # Initialize the current time

    # Create a copy of processes to preserve the original list
    processes_copy = processes.copy()

    waiting_times = []  # List to store waiting times for each process
    turnaround_times = []  # List to store turnaround times for each process

    while processes_copy:
        process = processes_copy.pop(0)

        if process.arrival_time <= current_time:
            # Calculate waiting time for the current process
            waiting_time = max(0, current_time - process.arrival_time)
            waiting_times.append(waiting_time)

            if process.burst_time <= time_quantum:
                # Process completes within the time quantum
                current_time += process.burst_time

                # Calculate turnaround time for the current process
                turnaround_time = waiting_time + process.burst_time
                turnaround_times.append(turnaround_time)

                # Append the process name and its start time to the schedule
                schedule.append((process.name, current_time - process.burst_time))
            else:
                # Process requires more time, reduce its burst time
                current_time += time_quantum
                process.burst_time -= time_quantum

                # Add the process back to the end of the queue
                processes_copy.append(process)
        else:
            # No processes are ready, increment the current time
            current_time += 1

    # Calculate average waiting and turnaround times
    average_waiting_time = sum(waiting_times) / len(waiting_times) if waiting_times else 0
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times) if turnaround_times else 0

    return schedule, average_waiting_time, average_turnaround_time



# Call the scheduling functions for different algorithms
fcfs_schedule, fcfs_avg_waiting_time, fcfs_avg_turnaround_time = fcfs_scheduling(processes)
sjf_schedule, sjf_avg_waiting_time, sjf_avg_turnaround_time = sjf_scheduling(processes)
print(processes)
priority_schedule, priority_avg_waiting_time, priority_avg_turnaround_time = priority_scheduling(processes)
round_robin_schedule, round_robin_avg_waiting_time, round_robin_avg_turnaround_time = round_robin_scheduling(processes)

# Print average waiting and turnaround times for all algorithms
print(f"FCFS - Average Waiting Time: {fcfs_avg_waiting_time:.2f}, Average Turnaround Time: {fcfs_avg_turnaround_time:.2f}")
print(f"SJF - Average Waiting Time: {sjf_avg_waiting_time:.2f}, Average Turnaround Time: {sjf_avg_turnaround_time:.2f}")
print(f"Priority - Average Waiting Time: {priority_avg_waiting_time:.2f}, Average Turnaround Time: {priority_avg_turnaround_time:.2f}")
print(f"Round Robin - Average Waiting Time: {round_robin_avg_waiting_time:.2f}, Average Turnaround Time: {round_robin_avg_turnaround_time:.2f}")

# Determine the suitable algorithm based on average turnaround time and average waiting time
average_times = {
    "FCFS": (fcfs_avg_waiting_time, fcfs_avg_turnaround_time),
    "SJF": (sjf_avg_waiting_time, sjf_avg_turnaround_time),
    "Priority": (priority_avg_waiting_time, priority_avg_turnaround_time),
    "Round Robin": (round_robin_avg_waiting_time, round_robin_avg_turnaround_time)
}

suitable_algorithm = min(average_times, key=lambda x: (average_times[x][1], average_times[x][0]))
print(f"Suitable Algorithm: {suitable_algorithm}")