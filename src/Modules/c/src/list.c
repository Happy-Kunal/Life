#include"list.h"
#include <string.h>

List createList()
{
  List return_list = {
    .num_of_elements = 0,
    .total_size = 0,
    .data = NULL,
    .size_of_data = NULL,
  };
  return return_list;
}

void appendList
(List *l, void *data, size_t size_of_data)
{
  if(l->data == NULL){
    l->data = malloc(size_of_data);
  }
  else{
    l->data = realloc(l->data, l->total_size + size_of_data);
  }

  if(l->size_of_data == NULL){
    l->size_of_data = malloc(sizeof(size_t));
  }
  else{
    l->size_of_data = realloc(l->size_of_data, 
        sizeof(size_t) * (l->num_of_elements + 1));
  }
  // passing the pointer to the memeory location where
  // the total_size ends aka last element
  memcpy(l->data + l->total_size, data, size_of_data);
  l->total_size += size_of_data;
  l->size_of_data[l->num_of_elements] = size_of_data;
  ++(l->num_of_elements);
}

void elementAtList
(const List *l, void *elem ,const size_t index)
{
  if(index >= l->num_of_elements){
    perror("Index out of range");
    exit(-1);
  }
  size_t size_of_elements_before_the_index = 0;
  for(size_t i = 0 ; i < index; ++i){
    size_of_elements_before_the_index += l->size_of_data[i];
  }
  memcpy(elem, l->data + size_of_elements_before_the_index , 
                l->size_of_data[index]);
}

void freeList
(List *l)
{
  if(l->data){
    free(l->data);
  }
  if(l->size_of_data){
    free(l->size_of_data);
  }
}
