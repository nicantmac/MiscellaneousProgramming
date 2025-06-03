#include <iostream>
#include <vector>
using namespace std;


int main() {

    vector<string> logos = {"Goober", "Tesla", "Pinhead"};
    logos.push_back("RayCharles");
    logos.push_back("Einstein");
    logos.push_back("Bomba");
    logos.pop_back();
    
    for (int i = 0; i < logos.size(); i++) {
        cout << logos[i] << endl;
    }
    return 0;
}
