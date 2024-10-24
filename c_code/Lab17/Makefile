CC = gcc

#FFLAGS = -Wall -std=c99 -Xpreprocessor -fopenmp
#LFLAGS = -lomp

LFLAGS = -lomp -L/opt/ homebrew/opt/libomp/lib
FFLAGS = -Wall -std=c99 -Xpreprocessor -fopenmp -I/opt/homebrew/opt/libomp/include

OBJECTS = omp_hello .o

main.exe: $(OBJECTS)
	$(CC) $(LFLAGS) $(OBJECTS) -o main.exe

%.o: %.c
	$(CC) $(FFLAGS) -c $<

clean:
	rm -f $(OBJECTS) *. exe