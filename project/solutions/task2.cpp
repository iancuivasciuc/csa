#include <iostream>
#include <utility>
using namespace std;

// Constants
const int MEMORY_SIZE = 1024;
const int MAX_FD = 255;

int memory[MAX_FD + 1][MEMORY_SIZE];
pair<int, int> files[MAX_FD + 1][2];

void show_file(int fd)
{
    cout << fd << ": ((" << files[fd][0].first << ", " << files[fd][0].second << "), (" << files[fd][1].first << ", " << files[fd][1].second << "))\n";
}

void show_memory()
{
    int row = 0;
    int col = 0;

    while (row < MAX_FD) {
        col = 0;
        while (col < MEMORY_SIZE) {
            if (memory[row][col] != 0) {
                int fd = memory[row][col];

                show_file(fd);
                col = files[fd][1].second;
            }

            col++;
        }

        row++;
    }
}

void add_to_memory(int fd, int row, int start, int end)
{
    for (int i = start; i <= end; i++)
        memory[row][i] = fd;
    files[fd][0] = {row, start};
    files[fd][1] = {row, end};
}

void add(int fd, int dim)
{
    int empty_col = 0;
    int row = 0;
    int col = 0;

    while (row < MAX_FD) {
        empty_col = 0;
        col = 0;
        while (col < MEMORY_SIZE) {
            if (memory[row][col] != 0) {
                empty_col = col + 1;
            } else if (memory[row][col] == 0 && (col - empty_col + 1 == dim)) {
                add_to_memory(fd, row, empty_col, col);
                show_file(fd);
                return;
            }

            col++;
        }

        row++;
    }

    show_file(fd);
}

void get(int fd)
{
    cout << "((" << files[fd][0].first << ", " << files[fd][0].second << "), (" << files[fd][1].first << ", " << files[fd][1].second << "))\n";
}

void del(int fd)
{
    int row = files[fd][0].first;
    int start = files[fd][0].second;
    int end = files[fd][1].second;

    for (int i = start; i <= end; i++)
        memory[row][i] = 0;
    files[fd][0] = {0, 0};
    files[fd][1] = {0, 0};
}

void defrag()
{
    int empty_row = 0;
    int empty_col = 0;
    int row = 0;
    int col = 0;

    while (row < MAX_FD) {
        col = 0;
        while (col < MEMORY_SIZE) {
            if (memory[row][col] != 0) {
                int fd = memory[row][col];
                int fd_len = files[fd][1].second - files[fd][0].second + 1;
                int empty_len = MEMORY_SIZE - empty_col;

                if (empty_len < fd_len) {
                    empty_row++;
                    empty_col = 0;
                }

                del(fd);
                add_to_memory(fd, empty_row, empty_col, empty_col + fd_len - 1);

                empty_col += fd_len;
                col += fd_len;
                continue;
            }

            col++;
        }

        row++;
    }
}

int main()
{
    int num_commands;

    cin >> num_commands;
    for (int i = 0; i < num_commands; i++) {
        int command;
        int num_files;
        int fd;
        int dim;

        cin >> command;

        switch (command) {
        case 1:
            cin >> num_files;
            for (int j = 0; j < num_files; j++) {
                cin >> fd >> dim;
                add(fd, (dim + 7) / 8);
            }
            break;
        case 2:
            cin >> fd;
            get(fd);
            break;
        case 3:
            cin >> fd;
            del(fd);
            show_memory();
            break;
        case 4:
            defrag();
            show_memory();
            break;
        default:
            exit(1);
        }
    }

    return 0;
}