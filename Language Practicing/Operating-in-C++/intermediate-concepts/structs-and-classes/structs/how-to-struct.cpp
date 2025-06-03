#include <iostream>
using namespace std;

struct Student {
    bool enrolled;
    double gpa;
    string name;
};

int main() {
    Student student1;
    student1.name = "Spongebob";
    student1.gpa = 3.25;
    student1.enrolled = true;

    Student student2;
    student2.name = "Patrick";
    student2.gpa = 2.25;
    student2.enrolled = false;

    cout << "Student #1" << endl;
    cout << "Name: " << student1.name << endl;
    cout << "Academic Performance: " << student1.gpa << endl;
    cout << "Enrollment status: " << student1.enrolled << endl;

    cout << "\nStudent #2" << endl;
    cout << "Name: " << student2.name << endl;
    cout << "Academic Performance: " << student2.gpa << endl;
    cout << "Enrollment status: " << student2.enrolled << endl;

    return 0;
}
