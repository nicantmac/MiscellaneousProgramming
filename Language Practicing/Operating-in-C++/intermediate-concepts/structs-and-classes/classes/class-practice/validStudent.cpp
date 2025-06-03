#include <iostream>
using namespace std;

class Student {
    // These below are what make up an object, which is attributes and methods. //

    public:
        // These below are attributes (data members).
        int numID;
        string firstName;
        string lastName;
        int gradYear;
        bool lunch;

        // These below are methods (member functions), because they're functions.
        // To call an object's methods, you use the dot notation (.):
        void eat() {
            if (lunch == true) {
                cout << "This student has eaten lunch already.";
            } else {
                cout << "This student hasn't been called to lunch.";
            }
        }
};

int main() {

    vector<Student> studentsList = {
            {12345, "John", "", 2025, false},
            {94430, "Sarah", "", 2025, false},
            {12774, "Mike", "", 2023, true},
            {41085, "Emily", "", 2024, true},
            {57823, "David", "", 2024, false}
    };

    cout << "Students print names below:" << endl;

    for (int i = 0; i < studentsList.size(); i++) {
        cout << (i + 1) << ". ";
        getline(cin, studentsList[i].firstName);
    }

    cout << endl;

    for (int i = 0; i < studentsList.size(); i++) {
        cout << "≈Student " << (i + 1) << "≈" << endl;
        cout << "Name: " << studentsList[i].firstName << " " << studentsList[i].lastName << endl;
        cout << "Student Info: (ID: " << studentsList[i].numID << ")," << " Graduating in " << studentsList[i].gradYear << "\n" << endl;
    }

    // getline creates a newline when finished
    // For calling an objects method, you don't have to cout the function.

    for (int i = 0; i < studentsList.size(); i++) {
        if (studentsList[i].lunch) {
            cout << studentsList[i].firstName << "'s section has attended lunchtime." << endl;
        } else {
            cout << studentsList[i].firstName << "'s section haven't been called to lunchtime yet." << endl;
        }
    }

    return 0;
}
