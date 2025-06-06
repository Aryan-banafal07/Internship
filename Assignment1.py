rows = 5

# Lower Triangular Pattern
print("Lower Triangular Pattern:")
for i in range(1, rows + 1):
    print("* " * i)
print()  # Blank line for separation

# Upper Triangular Pattern
print("Upper Triangular Pattern:")
for i in range(rows, 0, -1):
    print("* " * i)
print()  # Blank line for separation

# Pyramid Pattern
print("Pyramid Pattern:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
