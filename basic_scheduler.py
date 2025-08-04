import time

filename = "tasks.txt"
tasks = []
with open(filename)as f:
    for line in f:
        print(line)
        name, duration, deps = line.strip().split(',')
        tasks.append({
            'name': name,  # string
            'duration': int(duration),  # integer
            'dependencies': deps  # list of names
        })
print(tasks)
