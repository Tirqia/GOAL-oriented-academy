# 1. დაწერეთ ფუნქცია addNumbers, რომელიც იღებს ორ პარამეტრს და აბრუნებს მათ ჯამს.
def addNumbers(a, b):
    return a + b

# 2. დაწერეთ ფუნქცია multiplyNumbers, რომელიც იღებს ორ პარამეტრს და აბრუნებს მათ ნამრავლს.
def multiplyNumbers(a, b):
    return a * b

# 3. დაწერეთ ფუნქცია calculateRectangleArea, რომელიც იღებს სიგანესა და სიმაღლეს პარამეტრებად და აბრუნებს მართკუთხედის ფართობს.
def calculateRectangleArea(width, height):
    return width * height

# 4. დაწერეთ ფუნქცია calculateCircleCircumference, რომელიც იღებს რადიუსს პარამეტრად და აბრუნებს წრის სიგრძეს.
def calculateCircleCircumference(radius):
    return 2 * 3.14159 * radius

# 5. დაწერეთ ფუნქცია isEven, რომელიც იღებს რიცხვს პარამეტრად და აბრუნებს true-ს თუ ლუწია, false-ს თუ კენტია.
def isEven(number):
    return number % 2 == 0

# 6. დაწერეთ ფუნქცია findMax, რომელიც იღებს ორ რიცხვს პარამეტრად და აბრუნებს მათგან დიდს.
def findMax(a, b):
    return a if a > b else b

# 7. დაწერეთ ფუნქცია reverseString, რომელიც იღებს სტრიქონს პარამეტრად და აბრუნებს მის შებრუნებულ ვერსიას.
def reverseString(s):
    return s[::-1]

# 8. დაწერეთ ფუნქცია generateNumbersArray, რომელიც იღებს რიცხვს n პარამეტრად და აბრუნებს რიცხვების მასივს 1-დან n-მდე.
def generateNumbersArray(n):
    return list(range(1, n + 1))

# 9. დაწერეთ ფუნქცია sumArray, რომელიც იღებს რიცხვების მასივს პარამეტრად და აბრუნებს მასივის რიცხვების ჯამს.
def sumArray(arr):
    return sum(arr)

# 10. დაწერეთ ფუნქცია isPerfectNumber, რომელიც იღებს რიცხვს პარამეტრად და აბრუნებს true-ს თუ არის სრულყოფილი რიცხვი, false-ს თუ არა.
def isPerfectNumber(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

print(addNumbers(12, 33)) 
print(multiplyNumbers(42, 61))  
print(calculateRectangleArea(6, 12)) 
print(calculateCircleCircumference(5))  
print(isEven(16))  
print(findMax(156, 73))  
print(('ai ia ia ai'))  
print(generateNumbersArray(12))  
print(([1, 9, 2, 6, 5]))  
print(isPerfectNumber(3))  