while True:
    num_stars_bottom = int(input("Enter the number of stars in the bottom row of the shape:"))
    if num_stars_bottom % 2 == 1:
        break

rows = num_stars_bottom // 2 + 1
# Outer loop for each row
for i in range(rows):
    # Inner loop for spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Inner loop for stars
    for k in range(2 * i + 1):
        print("*", end="")

    # Move to the next line after each row is printed
    print()
