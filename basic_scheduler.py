import datetime as dt
import time
import os
import sys
import argparse
import ast

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input", help="Specify input file (tasks)", required=True)
    parser.add_argument("--validate", help="Validate file only", required=False, action="store_true")
    parser.add_argument("--run", help="Run the tasks", required=False, action="store_true")
    return parser.parse_args()

def validate_file(filename):
    if not os.path.exists(filename):
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    else:
        print(f"Found {filename}.")
    return filename

def load_file(valid_filename):
    tasks = []
    with open(valid_filename) as f:
        for line in f:
            name, duration, deps = line.strip().split(',')
            tasks.append({
                "name": str(name),  # string
                "duration": int(duration),  # integer
                "dependencies": ast.literal_eval(deps.strip())  # list of namfes
            })
    print("This is a valid tasks file")
    return tasks

def serial_mode(tasks_list):
    serial_duration = sum(i["duration"] for i in tasks_list)
    return serial_duration

def run(task_hash_map):
    start = dt.datetime.now()
    for name, task in task_hash_map.items():
        print(f"Running {name} for {task['duration']} seconds...")
        time.sleep(task['duration'])
    end = dt.datetime.now()
    total_duration = (end - start).total_seconds()
    return total_duration


def main():
    args = parser()
    filename = args.input
    print(f"File entered: {filename}")
    valid_filename = validate_file(filename)
    tasks_list = load_file(valid_filename) # this is a list
    print(tasks_list)
    task_hash_map = {i["name"]: i for i in tasks_list} # for now redundant
    print(task_hash_map)
    expected_duration = serial_mode(tasks_list)
    print(f"Estimated total runtime (no dependencies considered): {expected_duration} seconds")
    if args.validate:
        sys.exit(0)
    if args.run:
        # Run the task scheduler
        actual_duration = run(task_hash_map)
    delta_duration_exact = actual_duration - expected_duration
    delta_duration = round(delta_duration_exact,3)
    print(f"The difference from actual runtime to expected runtime is {delta_duration}")


if __name__ == "__main__":
    main()

