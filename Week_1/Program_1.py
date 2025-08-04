# Demonstrating different number data types in Python

# Integer
integer_num = 10
print("Integer:", integer_num)
print("Type:", type(integer_num))

# Float
float_num = 10.5
print("\nFloat:", float_num)
print("Type:", type(float_num))

# Complex Number
complex_num = 3 + 4j
print("\nComplex Number:", complex_num)
print("Type:", type(complex_num))

# Basic Operations
# Integer Operations
print("\nInteger Operations:")
print("Addition:", integer_num + 5)
print("Subtraction:", integer_num - 2)
print("Multiplication:", integer_num * 3)
print("Division:", integer_num / 2)

# Float Operations
print("\nFloat Operations:")
print("Addition:", float_num + 2.5)
print("Subtraction:", float_num - 1.5)
print("Multiplication:", float_num * 2)
print("Division:", float_num / 2)

# Complex Number Operations
print("\nComplex Number Operations:")
print("Addition:", complex_num + (1 + 2j))
print("Subtraction:", complex_num - (1 + 2j))
print("Multiplication:", complex_num * (1 + 2j))
print("Division:", complex_num / (1 + 2j))

# Summary of types
print("\nSummary of types:")
print("Integer type:", type(integer_num))
print("Float type:", type(float_num))
print("Complex type:", type(complex_num))
