#include <iostream>
using namespace std;

/*****
* Here below you'll understand these basic functionalities of pointers.
* - How pointers store memory addresses.
* - How to use the & (address-of) and * (dereference) operators.
*
*****/

int main() {
    // Let's start with accessing memory and deferencing variables
    int students = 100; 
    int *ptrStudents;
    ptrStudents = &students; // ptrStudents stores the address of students

    // Print the memory address stored in ptrStudents
    cout << "Memory address of (ptrStudents): " << ptrStudents << endl;

    // Now print the value and not the address for students, hint -> (dereference)
    cout << "Value pointed to by ptrStudents: " << *ptrStudents << endl;

    
    // Demonstrating pointer usage with strings
    string joeBiden = "1600 Pennsylvania Avenue NW, Washington, DC 20500";
    string roBoT = "1234 Doxxed Ln, Bolingborski, Saturn 33901";
    string *ptrBot = &roBoT; // Pointer storing the memory address of roBoT

    cout << "\nThe address for the Former President is " << joeBiden << endl;
    cout << "The address for the Robot is " << *ptrBot << endl; // Dereferencing pointer to get the value

    // Print the memory address of roBoT
    cout << "Memory address of roBoT (stored in pointBot): " << ptrBot << endl;

    // Change string through the pointer
    *ptrBot = "9876 Cyberspace Blvd, Matrix City, VR 40404";
    cout << "After changing *pointBot, new Robot address is: " << roBoT << endl;

    return 0;
}
