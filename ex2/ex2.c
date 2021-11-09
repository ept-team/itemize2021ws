
#include <stdio.h>
#include <stdlib.h>

void ignore_me_init_buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}


void win() {
    system("/bin/sh");
}

void main() {
    ignore_me_init_buffering();
    char input[50];
    
    puts("Write something");
    gets(input);
    
}