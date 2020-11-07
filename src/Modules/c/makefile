CC = cc
SRCDIR = src
OBJDIR = bin
TARGET = main # output binary
# do not edit below this line
SOURCES = $(shell find $(SRCDIR) -type f -name *.c)
OBJECTS = $(patsubst $(SRCDIR)/%,$(OBJDIR)/%,$(SOURCES:.c=.o))
	#Flags, Libraries
	CFLAGS      := -I. -c -g
	LIB         := 

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) -o $@ $^ $(LIB)

$(OBJDIR)/%.o : $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) -o $@ -c $(CFLAGS) $<

$(OBJDIR) :
	mkdir -p $@

.PHONY : all

clean:
	rm bin/*
	rm main

