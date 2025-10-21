# 📘 All-in-One: Python List Methods Demo

# 1. Create a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 2. append() → Add item to end
fruits.append("orange")
print("After append:", fruits)

# 3. insert() → Insert item at specific index
fruits.insert(1, "mango")
print("After insert:", fruits)

# 4. remove() → Remove item by value
fruits.remove("banana")
print("After remove:", fruits)

# 5. pop() → Remove and return item (last by default)
popped_item = fruits.pop()
print("Popped item:", popped_item)
print("After pop:", fruits)

# 6. index() → Find index of item
index_of_mango = fruits.index("mango")
print("Index of mango:", index_of_mango)

# 7. count() → Count occurrences
fruits.append("apple")
apple_count = fruits.count("apple")
print("Apple count:", apple_count)

# 8. sort() → Sort list alphabetically
fruits.sort()
print("Sorted list:", fruits)

# 9. reverse() → Reverse list order
fruits.reverse()
print("Reversed list:", fruits)

# 10. copy() → Make a shallow copy
copied_fruits = fruits.copy()
print("Copied list:", copied_fruits)

# 11. clear() → Remove all items
fruits.clear()
print("Cleared list:", fruits)

#12 
l=[3,2,55,7,63,6]
m = l.copy()
m[0] = 20 
print(l)
print(m)