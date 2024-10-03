# $ISUHPC / lectures / lecture12 / codes / stack / Makefile
CC = gcc
FFLAGS = -O3 -Wall
LFFLAG =
OBJECTS = main.o \
Option.o \
DisplayOptions.o \
Push.o \
Pop.o \
Peek.o \
DisplayStack.o \
GetStackSize.o \
DeleteStack.o

.PHONY: clean help

main.exe: $(OBJECTS)
	$(CC) $(LFLAGS) $(OBJECTS) -o main.exe

%.o: %.c
	$(CC) $(FFLAGS) -c $<

clean:
	rm -f $(OBJECTS) main.exe