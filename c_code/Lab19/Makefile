CC = gcc
FFLAGS = -Wall -std=c99 -fopenmp
LFLAGS = -lgomp
OBJECTS = lab19.o 

lab18.exe: $(OBJECTS)
        $(CC) $(LFLAGS) $(OBJECTS) -o lab19.exe

%.o: %.c
        $(CC) $(FFLAGS) -c $<

clean:
        rm -f $(OBJECTS) lab19.exe