#include <iostream>
using namespace std;

class Book {
    public:
        // Getter for the title attribute
        string getTitle() {
            return title;
        }
    
        // Getter for the author attribute
        string getAuthor() {
            return author;
        }
    
        // Getter for the price attribute
        double getPrice() {
            return price;
        }
    
        // Setter for the title attribute
        void setTitle(string newTitle) {
            title = newTitle;
        }
    
        // Setter for the author attribute
        void setAuthor(string newAuthor) {
            author = newAuthor;
        }
    
        // Setter for the price attribute
        void setPrice(double newPrice) {
            price = newPrice;
        }
    
    private:
        // Private data members with default values
        string title = "One Kid Wonder...where he is";
        string author = "John Doe";
        double price = 19.99;
};

int main() {
    Book book1; // Create an object of the Book class

    // Here, we display the original book information using getter methods
    cout << "The original title is: " << book1.getTitle() << endl;
    cout << "The original author is: " << book1.getAuthor() << endl;
    cout << "The original price is: $" << book1.getPrice() << endl;

    // Here, we update book information using setter methods
    book1.setTitle("Ginger But Not Man");
    book1.setAuthor("St. Nicholas");
    book1.setPrice(9.99);

    // Here, we display the updated book information using corresponding getter methods again
    cout << "\nThe updated title is: " << book1.getTitle() << endl;
    cout << "The updated author is: " << book1.getAuthor() << endl;
    cout << "The updated price is: $" << book1.getPrice() << endl;

    return 0;
}

/*****************************************************
Output:

The original title is: One Kid Wonder...where he is
The original author is: John Doe
The original price is: 19.99

The updated title is: Ginger But Not Man
The updated author is: St. Nicholas
The updated price is: 9.99
*****************************************************/
