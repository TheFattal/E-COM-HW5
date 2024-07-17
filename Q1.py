positive_count: int = 0
negative_count: int = 0
zero_count: int = 0
is_seven_divided: int = 0
last_positive: int = 0
last_negative: int = 0
is_any_positive: int = 0
is_any_negative: int = 0

for num in range(1, 11):
    number: int = int(input("Enter a number please:"))
    if number == -9999:
        print("You have entered a number that breaks the loop!")
        break
    if number < -1000 or number > 1000:
        continue
    if number > 0:
        positive_count += 1
        last_positive = number
    if number < 0:
        negative_count += 1
        last_negative += 1
    if number == 0:
        zero_count += 1
    if number % 7 == 0:
        is_seven_divided += 1
else:
    print(f"The number of positives is: {positive_count}")
    print(f"The number of negatives is: {negative_count}")
    print(f"The number of Zeroes is: {zero_count}")
    print(f"The number of The numbers that are divisible by seven without a remainder is: {is_seven_divided}")
    if is_any_positive != 0:
        print(f"The last positive is: {last_positive}")
    if is_any_negative != 0:
        print(f"The last negative is: {last_negative}")
