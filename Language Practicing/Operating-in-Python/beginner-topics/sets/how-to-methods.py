# Here is practice for essential and common Python set methods
# The set below is what will be manipulated
my_set = {1, 2, 3}
print("Original set:", my_set)

# ----- Basic Methods -----

# The .add() method adds values to the end of a set 
my_set.add(4)
print("After add(4):", my_set)

# The .remove() method removes a specific value within the set. However, will raise KeyError if element not found
my_set.remove(2)
print("After remove(2):", my_set)

# The method .discard() removes the specific value similar to .remove(), However, will NOT raise error if element not found
my_set.discard(10)  # No error even though 10 is not in set
print("After discard(10):", my_set)

# The .pop() method removes an arbitrary element. Reminder: for lists .pop() removes the last item because it's an ordered structure
popped = my_set.pop()
print(f"Popped element: {popped}")
print("After pop():", my_set)

# The .copy() method returns a shallow copy of a set
set_copy = my_set.copy()
print("Copy of set:", set_copy)

# The .clear() empties the values within a set
set_copy.clear()
print("After clear(), set_copy:", set_copy)

# --- Set Operations ---
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# union()
print("Union (A | B):", set_a.union(set_b))

# intersection()
print("Intersection (A & B):", set_a.intersection(set_b))

# difference()
print("Difference (A - B):", set_a.difference(set_b))

# symmetric_difference()
print("Symmetric difference (A ^ B):", set_a.symmetric_difference(set_b))

# --- Relationship Test Methods ---

set_c = {1, 2}
set_d = {1, 2, 3, 4}

# issubset()
print("Is set_c subset of set_d?", set_c.issubset(set_d))

# issuperset()
print("Is set_d superset of set_c?", set_d.issuperset(set_c))

# isdisjoint()
set_e = {5, 6}
print("Are set_c and set_e disjoint?", set_c.isdisjoint(set_e))
