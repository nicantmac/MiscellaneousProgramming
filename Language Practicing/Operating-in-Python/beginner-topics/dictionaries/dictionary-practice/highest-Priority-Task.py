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
# Step 1: Find the maximum priority value
    max_priority = max(tasks.values())

    # Step 2: Collect all task names with that priority
    top_tasks = []
    for task in tasks:
        if tasks[task] == max_priority:
            top_tasks.append(task)

    # Step 3: Sort those task names alphabetically
    top_tasks.sort()

    # Step 4: Choose the first one and remove it from the original dictionary
    top_task = top_tasks[0]
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
    print(get_highest_priority_task_manual(tasks))   # task2
    print(get_highest_priority_task_manual(tasks))   # task4
    print(get_highest_priority_task_manual(tasks))   # task3
    print("Remaining tasks:", tasks)                 # {'task1': 8, 'task5': 7}
