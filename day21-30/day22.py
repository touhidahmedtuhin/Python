# 📘 Introduction to Lists in Python

# 1. Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
empty_list = []

# 2. Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Looping through a list
print("\nAll fruits:")
for fruit in fruits:
    print(fruit)

# 4. Modifying elements
fruits[1] = "blueberry"
print("\nModified fruits:", fruits)

# 5. Adding items
fruits.append("orange")
fruits.insert(1, "mango")
print("\nAfter adding items:", fruits)

# 6. Removing items
fruits.remove("apple")
del fruits[0]
print("\nAfter removing items:", fruits)

# 7. List length
print("\nNumber of fruits:", len(fruits))

# 8. List comprehension
squares = [x**2 for x in range(5)]
print("\nSquares using list comprehension:", squares)

#another example
lst = []
for i in range(5):
    lst.append(i)
#this the same code 
lst = [i for i in range(5)]

# 9. Filtering with list comprehension
evens = [x for x in range(10) if x % 2 == 0]
print("\nEven numbers:", evens)
