# შექმენით ფუნქცია რომელსაც გადაეცემა ორი მნიშვნელობა,
# პირველი არის სია და მეორე არის სიიდან წასაშლელი მნიშვნელობა, გამოიყენეთ for ციკლი და იპოვეთ ყველაზე დიდი მნიშვნელობა,
# შემდეგ კი ეგ მნიშვნელობა სიიდან წაშალეთ, გამოიყენეთ remove მეთოდი, ბონუსი: remove მეთოდის მაგივრად დაწერეთ თვქენი ალგორითმი

# განსაზღვრეთ ფუნქცია უდიდესი რიცხვის საპოვნელად (find_largest):
def find_largest(numbers):
    # იგი ვარაუდობს, რომ სიაში პირველი რიცხვი ყველაზე დიდია (ყველაზე დიდი = რიცხვები[0]).
    largest = numbers[0]
    for num in numbers:  # შემდეგ ის იმეორებს თითოეულ რიცხვს სიაში
        # და განახლდება ყველაზე დიდი, თუ აღმოაჩენს რიცხვს, რომელიც აღემატება ახლანდელ უდიდეს.
        if num > largest:
            largest = num
    return largest  # საბოლოოდ, ის აბრუნებს ნაპოვნი ყველაზე დიდ რაოდენობას.


# განსაზღვრეთ ფუნქცია, რომ ამოიღოთ უდიდესი რიცხვი (remove_largest): ფუნქცია remove_largest იღებს ნომრების ჩამონათვალს შეყვანის სახით.
def remove_largest(numbers):
    # ის იყენებს find_largest ფუნქციას სიაში ყველაზე დიდი რიცხვის საპოვნელად.
    largest = find_largest(numbers)
    # შემდეგ ის ქმნის ახალ სიას (new_numbers) და იმეორებს თავდაპირველ სიაში თითოეულ რიცხვს.
    new_numbers = []
    for num in numbers:
        if num != largest:  # თითოეული რიცხვისთვის, თუ რიცხვი არ არის ნაპოვნი ყველაზე დიდი რიცხვის ტოლი, ის ამატებს რიცხვს ახალ სიას.
            new_numbers.append(num)
    # დაბოლოს, ის აბრუნებს ახალ სიას, რომელიც არის თავდაპირველი სია, სადაც ამოღებულია ყველაზე მეტი რაოდენობა.
    return new_numbers


numbers = [3, 13, 32, 59, 95]

result = remove_largest(numbers)
print(result)

'''

ფუნქცია find_largest იღებს რიცხვების ჩამონათვალს შეყვანის სახით.
იგი ვარაუდობს, რომ სიაში პირველი რიცხვი ყველაზე დიდია (ყველაზე დიდი = რიცხვები[0]).
შემდეგ ის იმეორებს თითოეულ რიცხვს სიაში და განახლდება ყველაზე დიდი, თუ აღმოაჩენს რიცხვს, რომელიც აღემატება ახლანდელ უდიდეს.
საბოლოოდ, ის აბრუნებს ნაპოვნი ყველაზე დიდ რაოდენობას.

განსაზღვრეთ ფუნქცია, რომ ამოიღოთ უდიდესი რიცხვი (remove_largest):
ფუნქცია remove_largest იღებს ნომრების ჩამონათვალს შეყვანის სახით.
ის იყენებს find_largest ფუნქციას სიაში ყველაზე დიდი რიცხვის საპოვნელად.
შემდეგ ის ქმნის ახალ სიას (new_numbers) და იმეორებს თავდაპირველ სიაში თითოეულ რიცხვს.
თითოეული რიცხვისთვის, თუ რიცხვი არ არის ნაპოვნი ყველაზე დიდი რიცხვის ტოლი, ის ამატებს რიცხვს ახალ სიას.
დაბოლოს, ის აბრუნებს ახალ სიას, რომელიც არის თავდაპირველი სია, სადაც ამოღებულია ყველაზე მეტი რაოდენობა.
გამოყენების მაგალითი:
განსაზღვრულია რიცხვების სამაგალითო სია (ნომრები = [23, 54, 12, 67, 8, 94, 32]).
ამ სიით გამოიძახება ფუნქცია remove_largest და შედეგი ინახება შედეგის ცვლადში.
შედეგი იბეჭდება კონსოლზე, სადაც ნაჩვენებია სია ყველაზე დიდი რიცხვის ამოღების შემდეგ.
საერთო ჯამში, ეს კოდი გვიჩვენებს, თუ როგორ უნდა იპოვოთ და ამოიღოთ სიიდან ყველაზე დიდი რიცხვი მორგებული ალგორითმის გამოყენებით, წაშლის მეთოდის გამოყენების ნაცვლად.
'''


def largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def remove_largest(numbers):
    largest = find_largest(numbers)
    new_numbers = []
    for num in numbers:
        if num != largest:
            new_numbers.append(num)
    return new_numbers


numbers = [3, 13, 32, 59, 53]

result = remove_largest(numbers)
print(result)


def remove_largest(numbers):
    largest = max(numbers)
    return [num for num in numbers if num != largest]


numbers = [3, 13, 32, 59, 95]
result = remove_largest(numbers)
print(result)
