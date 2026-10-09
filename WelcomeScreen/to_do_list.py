import json
import time
import os
if os.path.exists('tasks.json'):
    with open('tasks.json') as file:
        try:
            tasks = json.load(file)
        except json.decoder.JSONDecodeError:
            tasks = []
else:
    tasks = []

title = input("Enter your task: ")
priority = int(input("Enter a priority: 1. High 2. Medium 3. Low: "))
done = int(input("Enter a done: 1.yes 2.no"))
created_at = time.time()
if priority == 1:
    priority_data = "High"
elif priority == 2:
    priority_data = "Medium"
else:
    priority_data = "Low"
if done == 1:
    done_data = True
else:
    done_data = False
python_dict = {"title": title,'priority':priority_data,'done':done_data,'created_at':created_at}
tasks.append(python_dict)
with open('tasks.json', 'w') as outfile:
    json.dump(tasks, outfile,indent=4)
print('task is saved')

