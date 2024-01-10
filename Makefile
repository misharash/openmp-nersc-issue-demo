CC = gcc
LD = gcc
CFLAGS = -O0 -fPIC -Wall

# this allows building on Mac and Linux
ifeq ($(shell uname -s),Darwin)
# Here we use LLVM compiler to load the Mac OpenMP. Tested after installation commands:
# brew install llvm
# brew install libomp
# This may need to be modified with a different installation
ifndef HOMEBREW_PREFIX
HOMEBREW_PREFIX = /usr/local
endif
CFLAGS	+= -I$(HOMEBREW_PREFIX)/opt/libomp/include
LFLAGS	= -shared -L$(HOMEBREW_PREFIX)/opt/libomp/lib -lomp
else
# default (Linux) case
CFLAGS	+= -fopenmp
LFLAGS	= -shared -lgomp
endif

AUNTIE	= demo.so
AOBJS	= demo.o

.PHONY: main clean

main: $(AUNTIE)

$(AUNTIE):	$(AOBJS) Makefile
	$(LD) $(AOBJS) $(LFLAGS) -o $(AUNTIE)

clean:
	rm -f $(AUNTIE) $(AOBJS)

$(AOBJS): Makefile
