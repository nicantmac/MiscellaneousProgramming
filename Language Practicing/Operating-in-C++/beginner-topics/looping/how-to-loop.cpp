#include <iostream>
using namespace std;

void printArrayBackwards(int arr[], int size) {
    cout << "Array in Reverse: ";
    for (int i = size - 1; i >= 0; i--) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int countOccurrences(int arr[], int size, int target) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            count++;
        }
    }
    return count;
}

int main() {
    int size, target;

    // Taking array size input
    cout << "Enter the number of elements in the array: ";
    cin >> size;

    int arr[size];

    // Taking array input
    cout << "Enter " << size << " elements: ";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    // Printing array in reverse order
    printArrayBackwards(arr, size);

    // Asking for the target number to count
    cout << "Enter the number to count occurrences: ";
    cin >> target;

    // Counting occurrences of the target number
    int count = countOccurrences(arr, size, target);
    cout << "The number " << target << " appears " << count << " times in the array." << endl;

    return 0;
}
