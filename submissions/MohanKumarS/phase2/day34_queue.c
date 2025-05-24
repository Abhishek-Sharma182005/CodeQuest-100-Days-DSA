#include <stdio.h>
#define SIZE 20 // define the size for the Queue

int queue[SIZE];
int front = -1, rear = -1; // define the front and rear points

// Enqueue
void enqueue(int value)
{
    if (rear == SIZE - 1)
    {
        printf("Queue Overflow\n");
        return;
    }
    if (front == -1) 
        front = 0;
    rear = rear + 1;
    queue[rear] = value;
}

// Dequeue 
void dequeue()
{
    if (front == -1 || front > rear) 
    {
        printf("Queue Underflow\n");
        return;
    }
    front = front + 1;
}

// Display function
void display()
{
    if (front == -1 || front > rear) 
    {
        printf("Queue is empty.\n");
        return;
    }
    printf("Current Queue: ");
    for (int i = front; i <= rear; i++) 
    {
        printf("%d ", queue[i]);
    }
    printf("\n");
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    display();
    dequeue();
    dequeue();
    display();

    return 0;
}
