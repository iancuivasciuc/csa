# Checker for Computer Systems Architecture Laboratory Exercises

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

## Exercises List

The current exercises supported by the script are:

1. **prime**: Determine if a number is a prime.
2. **factorial**: Compute the factorial of a number using recursion.
3. **binsearch**: Perform binary search to find the last occurrence of a value in an array.
4. **palindrome**: Check if a given string is a palindrome.
5. **minimax**: Find the maximum of the column minimums in a matrix.

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
usage: checker.py [-h] [-s] [{prime,factorial,binsearch,palindrome,minimax}]

Check a list of assembly exercises.

positional arguments:
  {prime,factorial,binsearch,palindrome,minimax}
                        Specify an exercise to check or view its details.

options:
  -h, --help            show this help message and exit
  -s, --show            Display the summary, description, input/output format, and an example for the specified exercise.
```

### Test all exercises

```bash
$ python3 checker.py 
Checking prime     : ✔️ All tests passed!
Checking factorial : 🔴 File not found!
Checking binsearch : 🔴 File not found!
Checking palindrome: 🔴 File not found!
Checking minimax   : 🔴 File not found!
```

### Test a single exercise

```bash
$ python3 checker.py binsearch
Checking binsearch : 🔴 File not found!
```

### Show task summaries for all exercises

```bash
$ python3 checker.py -s
prime: Determine if a given number is a prime number.
factorial: Compute the factorial of a number using recursion.
binsearch: Find the last occurrence of an element in an array using binary search.
palindrome: Check if a given string is a palindrome.
minimax: Find the maximum of the column minimums in a matrix.
```

### Show detailed information for a single exercise

```bash
$ python3 checker.py -s minimax
Summary: Find the maximum of the column minimums in a matrix.

Description: The program should calculate the minimum value from each column of a matrix and then print the maximum of these minimum values.
- Input: The first line contains two integers `n` (number of rows) and `m` (number of columns), where 1 <= n, m <= 100.
The next `n` lines each contain `m` integers, the elements of the matrix, where -1e9 <= matrix[i][j] <= 1e9.
- Output: Print the maximum of the column minimums.

Example:
- Input: 3 3
1 2 3
4 5 6
7 8 9
- Output: 3
- Explanation: The minimums of the columns are: 1, 2, and 3. The maximum of these minimums is 3.
```
