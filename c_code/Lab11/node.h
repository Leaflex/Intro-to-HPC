#ifndef __NODE_H__
#define __NODE_H__

typedef struct node {
    int position;
    char value; // Changed from int to char
    struct node* next;
} node;

// Functions associated with struct node
int GetNumberOfNodes();
void GenerateList(node **head, const int num);
void Print(const int forward, const node* head);
void PrintList(const node* head);
void ReversePrintList(const node* head);
char GetKey(); // Changed return type to char
void SearchList(const node* head, const char key); // Changed parameter type to char
void DeleteList(node **head);

#endif
