#include <iostream>
using namespace std;

int main() {
    int students = 100;
    int *ptrStudents;
    ptrStudents = &students;
    students = 45;
    cout << *ptrStudents << endl;
}
