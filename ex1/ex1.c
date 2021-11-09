
#include <stdio.h>
int number;
int thing = 4;

int add(int a, int b) {
    return a+b;
}

void foo() {
        puts("hello from foo");
        int a = 0xdead;
        int b = 0xc0de;
        int res = add(a,b);
        printf("the result of %d + %d = %d\n", a,b,res);
    }


void main() {
    puts("hello from main");
    foo();
    number = 4;
    printf("%d\n", number );
}