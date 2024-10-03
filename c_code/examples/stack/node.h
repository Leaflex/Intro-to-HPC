#ifndef __NODE_H__
#define __NODE_H__

// Forward declaration of struct node
typedef struct node node;

struct node {
    int position;
    int value;
    node* next;
};

// Functions associated with struct node
int QueryOption();
void ExecuteOption( const int option , node ** top);
void DeleteStack(node ** top);
void DisplayOptions();
void DisplayStack(node* top);
void PrintNode(node* top);
void GetStackSize(node* top , int* stack_size);
int Peek(node* top);
void Pop(node ** top , int* output);
void Push(const int input , node ** top);

#endif
