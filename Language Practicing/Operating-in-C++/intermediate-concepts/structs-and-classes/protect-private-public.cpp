
#include <iostream>
using namespace std;

class Student {
    public:
        // Public members can be accessed directly in main() function with using the dot operator.
        string pub_member = "My classification is Public";

        // Getters are usually functions that
        // Getter for the protected member
        string getProtected() {
            return pro_member;
        }

        // Getter for the private member
        string getPrivate() {
            return priv_member;
        }

    protected:
        string pro_member = "My classification is Protected"; // Protected member

    private:
        string priv_member = "My classification is Private"; // Private member
};

int main() {
    // Create an instance (object) of the Student class
    Student student;

    // Accessing the public member directly
    cout << "Public: " << student.pub_member << endl;

    // Accessing protected and private members through getter methods
    cout << "Protected: " << student.getProtected() << endl;
    cout << "Private: " << student.getPrivate() << endl;

    return 0;
}


/*******************************************
Output:

Public: My classification is Public
Protected: My classification is Protected
Private: My classification is Private
*******************************************/
