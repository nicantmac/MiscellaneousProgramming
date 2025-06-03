#include <iostream>  // Includes the input-output stream library
using namespace std;  // Allows using standard library names without prefixing with "std::"

// Base class Animal
class Animal {
    public:
        bool alive = true;  // Public member variable indicating if the animal is alive

        // Public member function for eating
        void eat() {
            cout << "This animal is eating!" << endl;
        }
};

// Derived class Dog, inheriting from Animal
class Dog : public Animal {
    // The Dog class automatically has `alive` and `eat()` from Animal due to inheritance
    public:
        string bark = "bark bark";  // Public member variable for dog's bark sound
};

// Derived class Cat, inheriting from Animal
class Cat : public Animal {
    // The Cat class also inherits `alive` and `eat()` from Animal
    public:
        string meow = "meow meow";  // Public member variable for cat's meow sound

        // Public member function for scratching action
        void scratched() {
            cout << "I have claws and I'm going to scratch you." << endl;
        }
};

int main() {
    Dog doggy;     // Creates a Dog object named doggy
    Cat kitten;    // Creates a Cat object named kitten

    // Accessing and displaying properties of the doggy object
    cout << doggy.alive << endl;  // Outputs the alive status (true, shown as 1)
    cout << doggy.bark << endl;   // Outputs the bark sound
    doggy.eat();                  // Calls the eat() function inherited from Animal
    cout << endl;                 // Prints a newline for spacing

    // Accessing and displaying properties of the kitten object
    cout << kitten.alive << endl;  // Outputs the alive status (true, shown as 1)
    cout << kitten.meow << endl;   // Outputs the meow sound
    kitten.scratched();            // Calls the scratched() function specific to Cat

    return 0;  // Ends the program
}
