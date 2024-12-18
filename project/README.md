# Checker for Computer Systems Architecture Project

A Python script designed to test a predefined list of executables for common exercises in Computer Systems Architecture.

---

## Prerequisites
Ensure that **Python 3.9** (or later) is installed on your system.

### Installing Python3 on Ubuntu
Run the following commands to install Python3:
```bash
$ sudo apt update
$ sudo apt install python3
```

### Assembly Program Requirement

Assembly programs that are tested should flush stdout before exiting. This can be done with the following code:

```assembly
et_exit:
    pushl $0
    call fflush
    popl %eax
    
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
```

---

## Task List

1. **task1**: Unidimensional case.
2. **task2**: Bidimensional case.

---

## Usage

### Running the Script 

The script must be placed in the same directory as the executables to be tested.

### General Syntax

```bash
$ python3 checker.py [options] [exercise]
```

### Options

* `-h / --help`: Display help information for using the script.
* `-s / --show`: Show exercise details.

---

## Examples

### Help

```bash
$ python3 checker.py -h
usage: checker.py [-h] [-s] [{task1,task2}]

Check a list of assembly exercise.

positional arguments:
  {task1,task2}  Specify an exercise to check or view its details.

options:
  -h, --help     show this help message and exit
  -s, --show     Display the summary, description, input/output format.
```

### Test project

```bash
$ python3 checker.py 
Checking task1:
🔴 File not found!
task1: 0/50!

Checking task2:
🔴 File not found!
task2: 0/30!

Final grade: 0/80!
```