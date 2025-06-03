
#include <cmath>
#include <iostream>
#include <cstring>

using namespace std;

// Here we are going to work on Functions in C++

/******
*
* Let's practice Pointers and memory management that does the following:
*
* 1. Here create two functions; 1st function calculates the exponent of two numbers, and 2nd function evaluates if the result is higher or lower to the number fifty.
*
*******/

int exponentiate(int base, int exp) {

    int sum = pow(base, exp);
    return sum;
}

int lessThanFifty(int myNum, int num=50) {
    if (myNum > num) {
        cout << "Number is greater than the number 50" << endl;
    } else if (myNum < num) {
        cout << "Number is less than the number 50" << endl;
    } else {
        cout << "Number is equal to the number 50" << endl;
    }
}

int main() {

    cout<<"Enter an base: ";
    int baseNum;
    cin>>baseNum;

    cout<<"Enter an expo: ";
    int numExpo;
    cin>>numExpo;

    lessThanFifty(exponentiate(baseNum, numExpo));

    return 0;
}
