# 1. დაბეჭდე რიცხვები 1-დან 10-მდე:
for i in range(1, 11):
    print(i)

# 2. დაბეჭდე ლუწი რიცხვები 1-დან 20-მდე:
for i in range(2, 21, 2):
    print(i)

# 3. გამოთვალე და დაბეჭდე რიცხვების ჯამი 1-დან 100-მდე:
total_sum = 0
for i in range(1, 101):
    total_sum += i
print(f"რიცხვების ჯამი 1-დან 100-მდე არის {total_sum}")

# 4. დაბეჭდე 5-ის ჯერადი რიცხვები 50-მდე:
for i in range(5, 51, 5):
    print(i)

# 5. დაბეჭდე რიცხვები 10-დან 1-მდე:
for i in range(10, 0, -1):
    print(i)

# 6. გამოთვალე და დაბეჭდე რიცხვი 5-ის ფაქტორიალი:
factorial = 1
for i in range(1, 6):
    factorial *= i
print(f"რიცხვი 5-ის ფაქტორიალი არის {factorial}")

# 7. გამოთვალე და დაბეჭდე მასივში [1, 2, 3, 4, 5] რიცხვების ჯამი:
arr = [1, 2, 3, 4, 5]
array_sum = 0
for num in arr:
    array_sum += num
print(f"მასივის ჯამი არის {array_sum}")

# 8. მოძებნე და დაბეჭდე ყველაზე დიდი რიცხვი მასივში [10, 5, 8, 20, 2]:
arr = [10, 5, 8, 20, 2]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print(f"მასივში ყველაზე დიდი რიცხვი არის {largest}")

# 9. დაითვალე და დაბეჭდე ხმოვნების რაოდენობა მოცემულ სტრიქონში:
string = "Jumberikos utqvams movidneno ribaki bichebi"
vowels = "aeiou"
vowel_count = 0
for char in string:
    if char.lower() in vowels:
        vowel_count += 1
print(f"სტრიქონში ხმოვნების რაოდენობა არის {vowel_count}")

# 10. გამოთვალე და დაბეჭდე მასივში [10, 20, 30, 40, 50] რიცხვების საშუალო:
arr = [10, 20, 30, 40, 50]
total = 0
for num in arr:
    total += num
average = total / len(arr)
print(f"მასივის საშუალო არის {average}")
