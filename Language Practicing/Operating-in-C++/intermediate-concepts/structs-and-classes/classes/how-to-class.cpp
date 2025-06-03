#include <iostream>
using namespace std;

// Format: Practice keeping your classes and other def-functions above your int main function.

class Book1 {
public:
    string title;
    string author;
    int pages;
};

class Book2 {
    public:
        string title = "Lord Of The Rings";
        string author = "John R. Reuel Tolkein";
        int pages = 700;
};


int main () {
    Book1 book1; 
    // You can declare inside the class, then initialize in the main function.
    
    book1.title = "Harry Potter";
    book1.author = "JK Rowling";
    book1.pages = 835;

    Book2 book2;
    // You can declare and initialize inside the class, then just call in the int main function.
    cout << "Book #1:" << endl;
    cout << "Book#1 Title: " << book1.title << endl;
    cout << "Book#1 Written by: " << book1.author << endl;
    cout << "Book#1 has " << book1.pages << " pages."<< endl;
    cout << endl; // create a new line.
    cout << "Book #2:" << endl;
    cout << "Book#2 Title: " << book2.title << endl;
    cout << "Book#2 Written by: " << book2.author << endl;
    cout << "Book#2 has " << book2.pages << " pages."<< endl;

    return 0;
}
