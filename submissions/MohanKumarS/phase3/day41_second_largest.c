#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main() {
    int n;
    int *arr;
    int largest = INT_MIN, second_largest = INT_MIN;

    printf("Enter the number of elements: ");
    scanf("%d", &n);


    arr = (int *)malloc(n * sizeof(int));

    // Input
    printf("Enter %d numbers:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", (arr + i));  // using pointer arithmetic
    }

    // Find largest and second largest using pointers
    for (int i = 0; i < n; i++) {
        int value = *(arr + i);
        if (value > largest) {
            second_largest = largest;
            largest = value;
        } else if (value > second_largest && value != largest) {
            second_largest = value;
        }
    }

    if (second_largest == INT_MIN) {
        printf("No second largest number found (all numbers may be equal).\n");
    } 
    else {
        printf("The second largest number is: %d\n", second_largest);
    }

    return 0;
}
