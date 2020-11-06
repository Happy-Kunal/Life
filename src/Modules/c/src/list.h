// a generic doubly linked list implementation written in c
// by www.github.com/lunchspider

#ifndef LIST_H
#define LIST_H
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include<stdio.h>
typedef struct List List;

struct List{
  size_t num_of_elements;
  void *data;
  size_t total_size; // to store total size of void *data
  //using a size_t array to store the size of each the elements;
  size_t *size_of_data;
};

List createList();

void appendList(List *l, void *data, size_t size_of_data);

// copies the element at @param index in @param l in 
// the @param elem
// index starts at 0 and goto num_of_elements - 1
void elementAtList(const List *l, void *elem,const size_t index);

void changeElemList(List *l, const void *elem, const size_t index);

void freeList(List *l);
#endif
