#include <iostream>
#include <utility>
using namespace std;

// Constants
const int MEMORY_SIZE = 1024;
const int MAX_FD = 255;

int memory[MEMORY_SIZE];
pair<int, int> files[MAX_FD + 1];

void show_file(int fd)
{
    cout << fd << ": (" << files[fd].first << ", " << files[fd].second << ")\n";
}

void show_memory()
{
    int index = 0;

    while (index < MEMORY_SIZE) {
        if (memory[index] != 0) {
            int fd = memory[index];

            show_file(fd);
            index = files[fd].second;
        }

        index++;
    }
}

void add_to_memory(int fd, int start, int end)
{
    for (int i = start; i <= end; i++)
        memory[i] = fd;
    files[fd] = {start, end};
}

void add(int fd, int dim)
{
    int empty_index = 0;
    int index = 0;

    while (index < MEMORY_SIZE) {
        if (memory[index] != 0) {
            empty_index = index + 1;
        } else if (memory[index] == 0 && (index - empty_index + 1 == dim)) {
            add_to_memory(fd, empty_index, index);
            break;
        }

        index++;
    }

    show_file(fd);
}

void get(int fd)
{
    cout << "(" << files[fd].first << ", " << files[fd].second << ")\n";
}

void del(int fd)
{
    for (int i = files[fd].first; i <= files[fd].second; i++)
        memory[i] = 0;
    files[fd] = {0, 0};
}

void defrag()
{
    int empty_index = 0;
    int index = 0;

    while (index < MEMORY_SIZE) {
        if (memory[index] != 0) {
            if (empty_index != index) {
                int fd = memory[index];
                int fd_len = files[fd].second - files[fd].first + 1;

                del(fd);
                add_to_memory(fd, empty_index, empty_index + fd_len - 1);

                empty_index += fd_len;
                index += fd_len;
                continue;
            }

            empty_index++;
        }

        index++;
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