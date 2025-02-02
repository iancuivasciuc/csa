#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#define MAX_PATH_SIZE 256

int main(int argc, char **argv)
{
    char directory[MAX_PATH_SIZE] = {};
    char file[MAX_PATH_SIZE] = {};
    DIR *dir = NULL;
    struct dirent *entry = NULL;

    scanf("%s", directory);

    dir = opendir(directory);
    if (dir == NULL) {
        perror("Failed to open directory");
        return 1;
    }

    while ((entry = readdir(dir))) {
        /* Skip current and parent directories */
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;

        /* Build the full file path */
        snprintf(file, sizeof(file), "%s/%s", directory, entry->d_name);

        /* Open the file */
        int fd = open(file, O_RDONLY);

        if (fd == -1) {
            perror("Failed to open file");
            return 1;
        }

        struct stat file_stat;

        if (fstat(fd, &file_stat) == -1) {
            perror("Failed to get file stats");
            close(fd);
            return 1;
        }

        printf("File: %s, Descriptor: %d, Size: %d\n", file, fd, (int)file_stat.st_size);

        /* The file should always be closed, but not here. */
        /* close(fd); */
    }

    closedir(dir);

    return 0;
}