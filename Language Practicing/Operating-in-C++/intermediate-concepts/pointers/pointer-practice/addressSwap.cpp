
#include <iostream>
#include <cstring>
using namespace std;

// Here we are going to work on Arrays in C++

/******
*
* Let's practice Pointers and memory management that does the following:
*
* 1. Here create two variables that hold addresses instead of values and exchange them by making a function.
*
*******/


// This will be the function swaps two numbers.
void swap(int *swap_x, int *swap_y) {

    // Saving the first number in a safe place (a temporary variable named "temp1").
    int temp1 = *swap_x;
    // Saving the second number in another safe place (another temporary variable named "temp2").
    int temp2 = *swap_y;

    // Put the first number where the second number was.
    *swap_y = temp1;
    // And put the second number where the first number was.
    *swap_x = temp2;
}

int main() {
    // Make two numbers
    int x = 10;
    int y = 20;

    // Call the swap function, then print the numbers before and after the swapping.
    cout << "Before edit: " << x << " and "<< y << endl;

    swap(&x, &y); // Put the address in the function.

    cout << "After edit: " << x << " and "<< y << endl;

    return 0;
}
