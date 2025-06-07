#include <iostream>
using namespace std;

//Here we will work on various data types in C++

/****
*
* 1. In this file we will understand and practice many data types utilized in C++ 
*
* Int = "int" keyword is programmed to store positive and negative whole numbers.
* Double = "double" keyword is programmed to store decimal numbers with more digits for precision.
* Float = "float" keyword is programmed to store floating-point numbers, which are decimal numbers that can have fractional parts.
* Char = "char" keyword is programmed to store single character i.e. 'g' or 'n'. Char will always use single quotes '' instead of double quotes "".
* String = "string" keyword is programmed to store words/sentences i.e. "Jason Tatum" or "Howard University".
* Bool = "bool" keyword is programmed to store true and false values. (Remember; false == "zero" and true == "one")
*
*****/


int main() {
    
    // Just below we declare integer variables for birth year and age
    
    int birth_year, age; // Integers to store birth year and age
    int curr_year = 2024; // Integer to store the current year
    string name; // String variable to store the user's name

    // Asking for user's name
    cout << "What is your name? ";
    cin >> name;

    // Asking for user's birth year
    cout << "What year were you born in? ";
    cin >> birth_year;

    // Calculating age
    age = curr_year - birth_year;
    cout << "\nSince you were born in year " << birth_year << ", that makes you " << age << "." << endl;

    // Conditional statement to check if user is 21 or older
    if (age >= 21) {
        cout << "You are old enough to get in the bar. Drink safely!\n";
    } else {
        cout << "You are not old enough for the bar. The kid section is to your left.\n";
    }


    // Demonstrating different data types
    double movie_rating = 8.5; // Double for decimal values
    char first_letter = name[0]; // Character data type storing the first letter of the user's name
    bool likes_movies = true; // Boolean to represent a true/false value

    // Displaying the additional data types
    cout << "\nMovie Rating (example): " << movie_rating << endl;
    cout << "First letter of your name: " << first_letter << endl;
    cout << "Do you like movies? " << (likes_movies ? "Yes" : "No") << endl;

    // Demonstrating pointer usage
    string joeBiden = "1600 Pennsylvania Avenue NW, Washington, DC 20500";
    string roBoT = "1234 Doxxed Ln, Bolbingbor, Saturn 33901";
    string *pointBot = &roBoT; // Pointer storing the memory address of roBoT

    cout << "\nThe address for the Former President is " << joeBiden << endl;
    cout << "The address for the Robot is " << *pointBot << endl; // Dereferencing pointer to get the value

    return 0;
}
