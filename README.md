# scheduler_helper
This is a scheduler tool that can run tasks serially and parallel

## Instructions

Please review the following sections on how to get the repository and 
environment needed to use this job scheduler.

### Build Virtual Environment

This environment was built using Python `3.13.2` so all python packages
and modules should be forward compatible, but I do not guarantee
it will work on older versions of python.

This assignment is completed with python standard packages. You may use your python system-wide environment
, but it's recommended to set up/launch a virtual environment.

```
python -m venv <venv_name>
source <venv_name>/bin/activate
```

### Run Script

To run `basic_scheduler.py`, you want to learn about the options/arguments. All options are 
available by running `-h` option first.

```
(venv) (base) sotelobc@Brunos-MBP-2:~/scripts/scheduler_helper$ python basic_scheduler.py -h
usage: basic_scheduler.py [-h] --input INPUT [--validate]

options:
  -h, --help     show this help message and exit
  --input INPUT  Specify input file (tasks)
  --validate     Validate file only
```

#### Run validation only

This option lets you validate the entered tasks list file. It will also calculate
the estimate duration for a serial run. Concurrency/Parallel will be covered later. 

```
python basic_scheduler --input  tasks.txt --validate
```

#### Run scheduler

This option will run all tasks and calculate the logical path to complete all tasks. At the end, it 
compares the actual duration against the expected duration and print it

```
python basic_scheduler --input  tasks.txt --run
```

## Future work

The next steps in further improving this scheduler is to:

- Add task file validator for actual syntax checks (e.g. names of dependencies) on the text file. 
- Extend from serial independent to serial dependent capabilities; this would require knowledge of graph algorithm and leverage the hash map created
- Extend to concurrent and parallel features of this scheduler. This would be a little difficult with python standard libraries but I think it's possible.
For my own benefit, I would look into that as well as non-standard python packages that automate a lot of this.
