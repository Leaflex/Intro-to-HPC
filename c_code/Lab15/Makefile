CC = gcc
FFLAGS = -O3 -Wall -std=c99
LFFLAG = 
OBJECTS = main.o \
Hessenberg.o \
GetShift.o \
FindZero.o \
QRA.o \
matrix.o \
QRdecomp.o \
trimatrix.o

.PHONY: clean

main.exe: $(OBJECTS)
	$(CC) $(LFFLAG) $(OBJECTS) -o main.exe

%.o: %.c
	$(CC) $(FFLAGS) -c $<

clean:
	rm -f $(OBJECTS) main.exe
