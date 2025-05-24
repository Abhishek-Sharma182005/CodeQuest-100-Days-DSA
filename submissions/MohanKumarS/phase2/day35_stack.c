#include <stdio.h>
#define SIZE 20

int stack[SIZE];
int top = -1;

void push(int(value))
{
    if(top == SIZE - 1)
    {
        printf("Stack Overflow");
        return;
    }   
    else
    {
        top = top + 1;
        stack[top] = value;
    }
}

void pop()
{
    if(top == -1)
    {
        printf("Stack Underflow");
        return;
    }
    else
        top = top - 1;
}

void display()
{
    if (top == -1) 
    {
        printf("Stack is empty.\n");
        return;
    }
    for (int i = 0; i <= top; i++) 
    {
        printf("%d ", stack[i]);
    }
    printf("\n");
}

int main()
{
    push(100);
    push(200);
    push(300);
    printf("Before pop: ");
    display();
    pop();
    printf("After pop: ");
    display();

    return 0;
}