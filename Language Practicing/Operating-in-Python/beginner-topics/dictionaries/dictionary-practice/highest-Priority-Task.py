'''
PROMPT: Write a function get_highest_priority_task() that takes in a dictionary called tasks, 
where keys are task names and values are priorities (1–10, with 10 being the highest). 
Remove and return the task with the highest priority. 
If there's a tie, return the task name that comes first alphabetically.

Expected Output:
For tasks = {
    "task1": 8,
    "task2": 10,
    "task3": 9,
    "task4": 10,
    "task5": 7
}
→ Output: task2, task4, task3
→ Remaining dict: {"task1": 8, "task5": 7}
'''

# METHOD 1: Manual approach using loop and sorting for tie-breaker
def get_highest_priority_task_manual(tasks):
    # Find the max priority value
    max_priority = max(tasks.values())

    # Collect all tasks that have the max priority
    top_tasks = [task for task, priority in tasks.items() if priority == max_priority]

    # Choose the one that comes first alphabetically
    top_task = sorted(top_tasks)[0]

    # Remove it from the dictionary
    del tasks[top_task]

    return top_task

# METHOD 2: Single-line winner selection using sorted + lambda
def get_highest_priority_task_efficient(tasks):
    top_task = sorted(tasks.items(), key=lambda x: (-x[1], x[0]))[0][0]
    del tasks[top_task]
    return top_task


if __name__ == '__main__':
    tasks = {
        "task1": 8,
        "task2": 10,
        "task3": 9,
        "task4": 10,
        "task5": 7
    }

    print("Manual Method:")
    print(get_highest_priority_task_manual(tasks))  # task2
    print(get_highest_priority_task_manual(tasks))  # task4
    print(get_highest_priority_task_manual(tasks))  # task3
    print("Remaining tasks:", tasks)               # {'task1': 8, 'task5': 7}

    # Reset for efficient method
    tasks = {
        "task1": 8,
        "task2": 10,
        "task3": 9,
        "task4": 10,
        "task5": 7
    }

    print("\nEfficient Method:")
    print(get_highest_priority_task_efficient(tasks))  # task2
    print(get_highest_priority_task_efficient(tasks))  # task4
    print(get_highest_priority_task_efficient(tasks))  # task3
    print("Remaining tasks:", tasks)                   # {'task1': 8, 'task5': 7}
