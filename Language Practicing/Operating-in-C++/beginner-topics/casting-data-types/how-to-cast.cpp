#include <iostream>
#include <cstdlib>
using namespace std;

int main () {
    string currentAge = "3";
    cout << "The year of 2015, you were " << currentAge << " years-old." << endl;

    int newAge = stoi(currentAge);
    cout << "That means in 2020, you turned " << newAge + 5 << " years-old.";
    return 0;
}
