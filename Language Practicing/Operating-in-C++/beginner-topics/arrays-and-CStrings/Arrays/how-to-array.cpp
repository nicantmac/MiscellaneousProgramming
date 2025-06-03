/*
#include <iostream>
using namespace std;
int main() {
    int students = 100;
    int *ptrStudents;
    ptrStudents = &students;
    students = 45;
    cout << *ptrStudents << endl;
}*/

#include <iostream>
#include <string>
using namespace std;
string addWord(string*, string*);
int main(){
    string name = "John";
    string phrase = " is the best";
    string* word1 = &name;
    string* word2 = &phrase;
    cout << addWord(word1, word2) << endl;}
string addWord(string* word1, string* word2){
    return (*word1 + *word2);
}
