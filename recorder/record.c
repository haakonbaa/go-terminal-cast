#include <stdio.h>
#include <unistd.h> // fork
#include <signal.h>

int main() {
    pid_t child = fork();
    if (child < 0) {
        perror("fork failed");
        kill(0, SIGTERM);
    }
    printf("%d\n",child);
    return 0;
}