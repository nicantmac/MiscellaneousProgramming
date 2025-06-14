'''
PROMPT: Write a function restock_inventory() that takes in two dictionaries:
1. current_inventory – the current inventory of items
2. restock_list – a list of items and amounts to add to the inventory
** The function should return the updated inventory after restocking. **

Expected Output:
{
    "apples": 40,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}
'''

# METHOD 1: Manual dictionary update (beginner-friendly)
def restock_inventory_manual(current_inventory, restock_list):
    for item in restock_list:
        if item in current_inventory:
            current_inventory[item] += restock_list[item]
        else:
            current_inventory[item] = restock_list[item]
    return current_inventory

# METHOD 2: More efficient approach using .get()
def restock_inventory_efficient(current_inventory, restock_list):
    for item, amount in restock_list.items():
        current_inventory[item] = current_inventory.get(item, 0) + amount
    return current_inventory


if __name__ == '__main__':
    current_inventory = {"apples": 30, "bananas": 15, "oranges": 10}
    restock_list = {"oranges": 20, "apples": 10, "pears": 5}

    # Use .copy() method is there to avoid modifying the same original dictionary twice, since dictionaries are mutable in Python
    print("Manual Method:", restock_inventory_manual(current_inventory.copy(), restock_list))
    print("Efficient Method:", restock_inventory_efficient(current_inventory.copy(), restock_list))
