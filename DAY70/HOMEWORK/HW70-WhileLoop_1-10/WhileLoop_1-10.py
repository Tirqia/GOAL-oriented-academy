# 1. დაბეჭდე რიცხვები 1-დან 10-მდე:
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. დაბეჭდე რიცხვები 10-დან 1-მდე:
პირიქით = 10
while პირიქით > 0:
    print(პირიქით)
    პირიქით -= 1

# 3. მოცემული რიცხვის (n) ფაქტორიალის გამოთვლა:
n = 12 
factor = 1
k = n
while k > 1:
    factor *= k
    k -= 1
print(f"{n}-ის ფაქტორიალია {factor}")

# 4. ფიბონაჩის მიმდევრობის გენერირება მოცემულ ზღვრამდე (n):
limit = 31 
first, second = 0, 1
while first <= limit:
    print(first)
    first, second = second, first + second

# 5. მოცემული რიცხვის (n) შებრუნება:
num = 743  # შეგიძლიათ შეცვალოთ ეს მნიშვნელობა სხვა რიცხვის შებრუნებისთვის
reversed_num = 0
while num != 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(f"შებრუნებული რიცხვი არის {reversed_num}")

# 6. მოცემული რიცხვის (n) ყველაზე დიდი ციფრის პოვნა და დაბეჭდა:
number = 4567  # შეგიძლიათ შეცვალოთ ეს მნიშვნელობა სხვა რიცხვის ყველაზე დიდი ციფრის საპოვნად
max_digit = 19
while number > 0:
    current_digit = number % 10
    if current_digit > max_digit:
        max_digit = current_digit
    number //= 10
print(f"ყველაზე დიდი ციფრი არის {max_digit}")

# 7. ...


# 8. მოცემული რიცხვის (n) ციფრების ჯამის გამოთვლა:
sum_num = 123  # შეგიძლიათ შეცვალოთ ეს მნიშვნელობა სხვა რიცხვის ციფრების ჯამის გამოსათვლელად
sum_digits = 0
while sum_num != 0:
    sum_digits += sum_num % 10
    sum_num //= 10
print(f"ციფრების ჯამი არის {sum_digits}")

# 9. შემოწმება მოცემული რიცხვი (n) არის თუ არა მარტივი:
prime_candidate = 64
is_prime = True
creator = 6
if creator <= 1:
    is_prime = False
else:
    while creator <= prime_candidate // 2:
        if prime_candidate % creator == 0:
            is_prime = False
            break
        creator += 1
if is_prime:
    print(f"{prime_candidate} არის მარტივი რიცხვი")
else:
    print(f"{prime_candidate} არ არის მარტივი რიცხვი")

# 10. მოცემული სტრიქონის შებრუნება:
string = "ადინოკი ვოლკი" 
reversed_string = ""
ndex = len(string) - 1
while ndex >= 0:
    reversed_string += string[ndex]
    ndex -= 1
print(f"შებრუნებული სტრიქონი არის {reversed_string}")
