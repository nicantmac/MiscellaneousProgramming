#include <iostream>
using namespace std;

double x = 52.75, y = 28.31, z = 109.99;
string str;
int points = 500;
int charge;

int main() {
    cout << "Enter customer's name on the bill: \n";
    cin >> str;
    cout << x + y + z;

    if (points >= 200) {
        cout << "\nEnter number of points: ";
        cin >> points;
        cout << "For every 100 points, deduct $5.00 from the original charge on the bill \n";
    }
    else (points < 200); {
        cout << "No deductions from bill \n";
    }
    cout << "Enter new the charge on the bill after deductions: ";
    cin >> charge;
    return 0;
}
