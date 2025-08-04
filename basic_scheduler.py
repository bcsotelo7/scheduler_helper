import time
import pathlib
import os
import sys
import argparse
import ast

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', help="Specify input file (tasks)", required=True)
    return parser.parse_args()

def validate_file(filename):
    if not os.path.exists(filename):
        print(f'Error: File {filename} not found.')
        sys.exit(1)
    else:
        print(f"Found {filename}.")
    return filename

def load_file(valid_filename):
    tasks = []
    with open(valid_filename) as f:
        for line in f:
            print(line)
            name, duration, deps = line.strip().split(',')
            tasks.append({
                'name': name,  # string
                'duration': int(duration),  # integer
                'dependencies': ast.literal_eval(deps.strip())  # list of names
            })
    return tasks

def serial_mode(tasks_list):
    serial_duration = sum(i['duration'] for i in tasks_list)
    return serial_duration

def main():
    args = parser()
    filename = args.input
    print(f'File entered: {filename}')
    valid_filename = validate_file(filename)
    tasks_list = load_file(valid_filename)
    serial_duration = serial_mode(tasks_list)
    print(f"Estimated total runtime (no dependencies considered): {serial_duration} seconds")


if __name__ == "__main__":
    main()

