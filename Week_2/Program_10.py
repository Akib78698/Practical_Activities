# Number of total rows for the full pattern
n = 5

# First half of the pattern (increasing stars)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Second half of the pattern (decreasing stars)
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
