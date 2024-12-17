#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
    int file_descriptor;
    char buffer[100];

    // apel de sistem pentru deschiderea unui fisier
    file_descriptor = open("input.txt", O_RDONLY);

    if (file_descriptor < 0)
    {
        perror("Eroare la deschiderea fisierului");
        return 1;
    }

    // apel de sistem pentru citirea datelor din fis, ier
    ssize_t bytes_read = read(file_descriptor, buffer, sizeof(buffer) - 1);

    printf("Bytes read: %ld\n", bytes_read);

    if (bytes_read < 0)
    {
        perror("Eroare la citire");
        return 1;
    }

    buffer[bytes_read] = '\0'; // terminare string
    // afisam continutul citit
    printf("Date citite: %s\n", buffer);
    // inchidem fisierul
    close(file_descriptor);

    return 0; 
}