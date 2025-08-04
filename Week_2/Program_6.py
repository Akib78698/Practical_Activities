# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("First element:", my_tuple[0])  # Output: 1
print("Last element:", my_tuple[-1])  # Output: 5

# Slicing a tuple
sliced_tuple = my_tuple[1:4]  # This will get elements from index 1 to 3
print("Sliced tuple (index 1 to 3):", sliced_tuple)  # Output: (2, 3, 4)

# Tuple concatenation
another_tuple = (6, 7, 8)
combined_tuple = my_tuple + another_tuple
print("Combined tuple:", combined_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# Tuple repetition
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking membership
print("Is 3 in my_tuple?", 3 in my_tuple)  # Output: True
print("Is 10 in my_tuple?", 10 in my_tuple)  # Output: False

# Unpacking a tuple
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)  # Output: 1 2 3 4 5

# Length of a tuple
print("Length of my_tuple:", len(my_tuple))  # Output: 5

# Nested tuples
nested_tuple = (1, (2, 3), 4)
print("Nested tuple:", nested_tuple)  # Output: (1, (2, 3), 4)
print("Accessing nested element:", nested_tuple[1][0])  # Output: 2
