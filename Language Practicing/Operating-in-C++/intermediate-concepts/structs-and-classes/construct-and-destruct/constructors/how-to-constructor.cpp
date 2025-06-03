#include <iostream>
using namespace std;

class Alien {
    public:
        int strength;
        string planet;
        string pieces;

    // The default constructor sets the object's attributes (member variables):
    Alien() {
        spieces = "Demigorgan";
        planet = "Zorgbog";
        strength = 10000;
    }
};

int main() {

    Alien alien1; // This line creates (instantiates) an Alien object and calls the default constructor

    cout << "*** Scientist Discover ***" << endl;
    cout << "Alien spieces: " << alien1.spieces << endl;
    cout << "Origination: " << alien1.planet << endl;
    cout << "Lab Tested Strength: " << alien1.strength;

    return 0;
}
