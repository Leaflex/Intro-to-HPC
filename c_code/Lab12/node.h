#ifndef __NODE_H__
#define __NODE_H__

// Forward declaration of struct node
typedef struct node node;

struct node {
    int position;
    char Suit[9];
    char Card[6];
    node* next;
};

// Functions associated with struct node
int QueryOption();
void ExecuteOption( const int option , node** top);
void DeleteStack(node** top);
void DisplayOptions();
void DisplayStack(node* top);
void PrintNode(node* top);
void GetStackSize(node* top , int* stack_size);
void Peek(node* top);
void Pop(node** top, char* suit, char* card);
void Push(const char* suit, const char* card, node** top);

#endif
