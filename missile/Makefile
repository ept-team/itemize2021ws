CC=gcc
FLAGS = -no-pie 
all: dyn stat
dyn:
	$(CC) $(FLAGS) -o dynamic/missile  missile.c  

stat:
	$(CC) -static $(FLAGS) -o static/missile-static  missile.c  