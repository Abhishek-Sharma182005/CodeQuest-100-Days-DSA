#include <stdio.h>  // for input and output operations -> printf(), scanf()
#include <stdlib.h> // for dynamic memory management -> malloc(), calloc(), calloc(),free()

// to define a structure node
struct node{
    int data;          // data -> is an integer
    struct node* next; // next -> points the another structure of the same type node
};

struct node* START = NULL;

// create a newNode
struct node* createNode()
{
   return (struct node*) malloc (sizeof (struct node));
}

void insertAtEnd(int data)
{
    struct node* newNode = createNode();
    newNode -> data = data;
    newNode -> next = NULL;
    if(START == NULL)
        START = newNode;
    else
    {
        struct node* temp = START; // temp struct to traverse the array -> find the last node
        while(temp -> next != NULL)
        {
            temp = temp -> next;
        }
        // at the end of loop, we find the last node
        temp -> next = newNode; // assign the next of last list with newNode address
    }
    printf("Node Inserted...\n");    
}

// to print the list
void printList(struct node *node) {
    printf("Current List: ");
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}

int main() {
    int choice, data, element;

    while (1) {
        printf("\n--- Linked List Operations ---\n");
        printf("1. Insert\n");
        printf("2. Print List\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data to insert at end: ");
                scanf("%d", &data);
                insertAtEnd(data);
                break;
            case 2:
                printList(START);
                break;
            case 0:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice. Try again.\n");
        }
    }

    return 0;
}