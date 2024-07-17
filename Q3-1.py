number: int = int(input("Please insert a number:"))
# Using nested loops to print the pattern
for i in range(1, number+1):  # Loop for rows 1 to 5
    for j in range(1, i + 1):  # Loop for columns, increasing order
        print(j, end="")
    print()

for i in range(number - 1, 0, -1):  # Loop for rows 4 to 1
    for j in range(1, i + 1):  # Loop for columns, decreasing order
        print(j, end="")
    print()
