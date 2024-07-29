# 1. ფუნქცია, რომელიც გამოყოფს რიცხვი პოზიტიურ, ნეგატიურ ან ნულოვანი
def checkNumber(num):
    if num > 0:
        print("რიცხვი პოზიტიურია.")
    elif num < 0:
        print("რიცხვი ნეგატიურია.")
    else:
        print("რიცხვი ნულია.")

# 2. ფუნქცია, რომელიც ადგენს არის თუ არა რიცხვი ლუწი ან კენტი
def checkEvenOdd(num):
    if num % 2 == 0:
        print("რიცხვი ლუწია.")
    else:
        print("რიცხვი კენტია.")

# 3. ფუნქცია, რომელიც ადგენს არის თუ არა წელი ხანმოკლე
def checkLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} არის ხანმოკლე წელი.")
    else:
        print(f"{year} არ არის ხანმოკლე წელი.")

# 4. ფუნქცია, რომელიც აბრუნებს ორ რიცხვს შორის დიდს
def findLarger(a, b):
    if a > b:
        return a
    else:
        return b

# 5. ფუნქცია, რომელიც აბრუნებს სამ რიცხვს შორის პატარაას
def findSmallest(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c

# 6. ფუნქცია, რომელიც განსაზღვრავს არის თუ არა სტრიქონი ცარიელი
def isEmptyString(s):
    if len(s) == 0:
        print("სტრიქონი ცარიელია.")
    else:
        print("სტრიქონი არ არის ცარიელი.")

# 7. ფუნქცია, რომელიც ადგენს არის თუ არა სტრიქონი პალინდრომი
def isPalindrome(s):
    if s == s[::-1]:
        print("სტრიქონი არის პალინდრომი.")
    else:
        print("სტრიქონი არ არის პალინდრომი.")

# 8. ფუნქცია, რომელიც გარდაქმნის ნომერულ შეფასებას (0-100) ასო-შეფასებაში (A, B, C და ა.შ.)
def convertToLetterGrade(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    else:
        return "F"

# 9. ფუნქცია, რომელიც ადგენს არის თუ არა რიცხვი თავდაპირველი
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 10. ფუნქცია, რომელიც გარდაქმნის ცელსიუსიდან ფარენჰაიტში ტემპერატურას
def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

print("1. checkNumber(5):")
checkNumber(5)  # გამოტანილი: რიცხვი პოზიტიურია.

print("2. checkEvenOdd(7):")
checkEvenOdd(7)  # გამოტანილი: რიცხვი კენტია.

print("3. checkLeapYear(2024):")
checkLeapYear(2024)  # გამოტანილი: 2024 არის ხანმოკლე წელი.

print("4. findLarger(10, 15):", findLarger(10, 15))  # გამოტანილი: 15

print("5. findSmallest(10, 20, 5):", findSmallest(10, 20, 5))  # გამოტანილი: 5

print("6. isEmptyString(''):")
isEmptyString('')  # გამოტანილი: სტრიქონი ცარიელია.

print("7. isPalindrome('madam'):")
isPalindrome('madam')  # გამოტანილი: სტრიქონი არის პალინდრომი.

print("8. convertToLetterGrade(85):", convertToLetterGrade(85))  # გამოტანილი: B

print("9. isPrime(11):", isPrime(11))  # გამოტანილი: True

print("10. celsiusToFahrenheit(25):", celsiusToFahrenheit(25))  # გამოტანილი: 77.0
