# Program to create, append, and remove elements from a list

# Step 1: Create a list
my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)

# Step 2: Append elements to the list
my_list.append(6)  # Appending a single element
print("List after appending 6:", my_list)

my_list.append(7)  # Appending another element
print("List after appending 7:", my_list)

# Step 3: Remove elements from the list
my_list.remove(3)  # Removing a specific element
print("List after removing 3:", my_list)

# Removing the last element using pop
removed_element = my_list.pop()  # This will remove and return the last element
print("Removed element:", removed_element)
print("List after popping the last element:", my_list)

# Step 4: Clear the entire list
my_list.clear()
print("List after clearing all elements:", my_list)
