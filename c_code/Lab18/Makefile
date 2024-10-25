CC = gcc
LFLAGS = -lomp -L/opt/ homebrew/opt/libomp/lib
FFLAGS = -Wall -std=c99 -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include
OBJECTS = lab18.o

lab18.exe: $(OBJECTS)
	$(CC) $(LFLAGS) $(OBJECTS) -o lab18.exe

%.o: %.c
	$(CC) $(FFLAGS) -c $<

clean:
	rm -f $(OBJECTS) lab18.exe
