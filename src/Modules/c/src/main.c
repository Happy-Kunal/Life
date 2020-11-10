#include "arena.h"
#include"list.h"
#include <stdio.h>
int main()
{
  List l = createList();
  size_t i = 7;
  appendList(&l, &i , sizeof i);
  size_t j;
  elementAtList(&l, &j, 0);
  printf("%zu\n",j);
  freeList(&l);
  return 0;
}