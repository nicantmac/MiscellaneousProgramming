#include <iostream>
using namespace std;

// Node class represents a single node in the linked list
class Node {
public:
    int data;      // Data stored in the node
    Node* next;    // Pointer to the next node

    // Constructor to initialize node with data
    Node(int val) {
        data = val;
        next = nullptr;  // Initially, the next pointer is null
    }
};

// LinkedList class represents the entire linked list
class LinkedList {
public:
    Node* head;  // Pointer to the first node of the list

    // Constructor to initialize an empty list
    LinkedList() {
        head = nullptr;
    }

    // Insert a node at the end of the list
    void append(int data) {
        Node* newNode = new Node(data);  // Create a new node with the given data
        if (head == nullptr) {
            head = newNode;  // If the list is empty, make newNode the head
            return;
        }

        // Traverse to the last node
        Node* last = head;
        while (last->next != nullptr) {
            last = last->next;
        }

        // Point the last node to the new node
        last->next = newNode;
    }

    // Print the entire list
    void printList() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "nullptr" << endl;
    }

    // Destructor to free memory
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* nextNode = current->next;
            delete current;  // Free memory of the current node
            current = nextNode;
        }
    }
};

// Main function to test the LinkedList class
int main() {
    LinkedList list;

    // Append some values to the list
    list.append(10);
    list.append(20);
    list.append(30);

    // Print the list
    cout << "Linked List: ";
    list.printList();

    return 0;
}
