# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing elements
print("Name:", my_dict["name"])  # Output: Alice
print("Age:", my_dict["age"])    # Output: 30

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"
print("Updated dictionary:", my_dict)

# Updating an existing key
my_dict["age"] = 31
print("Updated age:", my_dict["age"])  # Output: 31

# Deleting a key-value pair
del my_dict["city"]
print("Dictionary after deleting 'city':", my_dict)

# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary.")

# Iterating through keys
print("Keys in the dictionary:")
for key in my_dict:
    print(key)

# Iterating through values
print("Values in the dictionary:")
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
print("Key-value pairs in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Getting the number of items in the dictionary
print("Number of items in the dictionary:", len(my_dict))  # Output: 3

# Creating a nested dictionary
nested_dict = {
    "person": {
        "name": "Bob",
        "age": 25
    },
    "location": "Los Angeles"
}
print("Nested dictionary:", nested_dict)
print("Accessing nested value:", nested_dict["person"]["name"])  # Output: Bob
