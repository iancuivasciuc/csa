import numpy as np
import math
import sys

# Constants
MEMORY_SIZE = 1024
MAX_FD = 256

memory = np.zeros((MAX_FD, MEMORY_SIZE), 'uint16')
files = np.zeros((MAX_FD, 2, 2), 'uint16')


def add(fd, dim):
    if dim < 2 or files[fd, 1, 1] != 0:
        return

    row = 0
    while row < MAX_FD:
        left, right = 0, 0
        while left < MEMORY_SIZE:
            while left < MEMORY_SIZE and memory[row, left] != 0:
                left += 1

            right = left
            while right < MEMORY_SIZE and memory[row, right] == 0:
                if right - left + 1 == dim:
                    memory[row, left:right + 1] = fd
                    files[fd, 0] = [row, left]
                    files[fd, 1] = [row, right]
                    return

                right += 1

            left = right

        row += 1


def get(fd, fout):
    fout.write(f"(({files[fd, 0, 0]}, {files[fd, 0, 1]}), ({files[fd, 1, 0]}, {files[fd, 1, 1]}))\n")


def delete(fd):
    memory[files[fd, 0, 0], files[fd, 0, 1]:files[fd, 1, 1] + 1] = 0
    files[fd, 0] = [0, 0]
    files[fd, 1] = [0, 0]


def compress_row(row, upper_empty_len, upper_empty_rows):
    empty_len = 0
    column = 0
    first_fd = True

    while column < MEMORY_SIZE:
        if memory[row, column] != 0:
            fd = memory[row, column]
            fd_len = files[fd, 1, 1] - files[fd, 0, 1] + 1

            if first_fd is True:
                if row - upper_empty_rows != 0 and fd_len <= upper_empty_len:
                    upper_empty_start = MEMORY_SIZE - upper_empty_len

                    memory[row, column:column + fd_len] = 0
                    memory[row - upper_empty_rows - 1, upper_empty_start:upper_empty_start + fd_len] = fd
                    files[fd, 0] = [row - upper_empty_rows - 1, upper_empty_start]
                    files[fd, 1] = [row - upper_empty_rows - 1, upper_empty_start + fd_len - 1]

                    upper_empty_len -= fd_len
                    empty_len += fd_len
                    column += fd_len

                    continue

                first_fd = False

            if upper_empty_rows != 0:
                memory[row, column:column + fd_len] = 0
                memory[row - upper_empty_rows, 0:fd_len] = fd
                files[fd, 0] = [row - upper_empty_rows, 0]
                files[fd, 1] = [row - upper_empty_rows, fd_len - 1]

                first_fd = True
                upper_empty_rows -= 1
                upper_empty_len = MEMORY_SIZE - fd_len
                empty_len += fd_len
                column += fd_len

                continue

            if empty_len != 0:
                memory[row, column:column + fd_len] = 0
                memory[row, column - empty_len:column - empty_len + fd_len] = fd
                files[fd, 0, 1] -= empty_len
                files[fd, 1, 1] -= empty_len

                column += fd_len
                continue
        else:
            empty_len += 1

        column += 1

    if empty_len == MEMORY_SIZE:
        return upper_empty_len, upper_empty_rows + 1
    else:
        return empty_len, upper_empty_rows


def defragmentation():
    upper_empty_len, upper_empty_rows = MEMORY_SIZE, 0
    for row in range(MAX_FD):
        upper_empty_len, upper_empty_rows = compress_row(row, upper_empty_len, upper_empty_rows)


def show_memory(fout):
    row, col = 0, 0

    while row < MAX_FD:
        col = 0
        while col < MEMORY_SIZE:
            if memory[row, col] != 0:
                fd = memory[row, col]
                fout.write(f"{fd}: (({files[fd, 0, 0]}, {files[fd, 0, 1]}), ({files[fd, 1, 0]}, {files[fd, 1, 1]}))\n")
                col = files[fd, 1, 1]

            col += 1

        row += 1


def solve(input_file, output_file):
    fin = open(input_file, 'r')
    fout = open(output_file, 'w')

    num_commands = int(fin.readline().strip())
    for _ in range(num_commands):
        command = int(fin.readline().strip())
        if command == 1:
            num_files = int(fin.readline().strip())
            for _ in range(num_files):
                fd = int(fin.readline().strip())
                dim = float(fin.readline().strip())
                add(fd, math.ceil(dim / 8.0))

            show_memory(fout)
        elif command == 2:
            fd = int(fin.readline().strip())
            get(fd, fout)
        elif command == 3:
            fd = int(fin.readline().strip())
            delete(fd)
            show_memory(fout)
        elif command == 4:
            defragmentation()
            show_memory(fout)

    fin.close()
    fout.close()


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 solver.py <input.txt> <output.txt>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    solve(input_file, output_file)


if __name__ == '__main__':
    main()
