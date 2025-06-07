#include <iostream>
using namespace std;

/*****
* Here below you'll understand these basic functionalities of pointers.
* - How pointers store memory addresses.
* - How to use the & (address-of) and * (dereference) operators.
*
*****/

int main() {
    int students = 100; 
    int *ptrStudents;
    ptrStudents = &students; // ptrStudents stores the address of students

    // Print the memory address stored in ptrStudents
    cout << "Memory address of students (stored in ptrStudents): " << ptrStudents << endl;

    // Print the value at that address (dereference)
    cout << "Value pointed to by ptrStudents: " << *ptrStudents << endl;

    // Change the value of students
    students = 45;
    cout << "After changing students to 45, value pointed to by ptrStudents: " << *ptrStudents << endl;

    // Change the value through the pointer!
    *ptrStudents = 77;
    cout << "After changing *ptrStudents to 77, students is now: " << students << endl;

    // Demonstrating pointer usage with strings
    string joeBiden = "1600 Pennsylvania Avenue NW, Washington, DC 20500";
    string roBoT = "1234 Doxxed Ln, Bolbingbor, Saturn 33901";
    string *pointBot = &roBoT; // Pointer storing the memory address of roBoT

    cout << "\nThe address for the Former President is " << joeBiden << endl;
    cout << "The address for the Robot is " << *pointBot << endl; // Dereferencing pointer to get the value

    // Print the memory address of roBoT
    cout << "Memory address of roBoT (stored in pointBot): " << pointBot << endl;

    // Change string through the pointer
    *pointBot = "9876 Cyberspace Blvd, Matrix City, VR 40404";
    cout << "After changing *pointBot, new Robot address is: " << roBoT << endl;

    return 0;
}
