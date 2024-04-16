# book1 = "book1"
# book2 = "book2"
# book3 = "book3"
# book4 = "book4"
# book5 = "book5"
# book6 = "book6"
# book7 = "book7"
# book8 = "book8"
# book9 = "book9"
# book10 = "book10"

# disscount10 = 0, 1
# disscount20 = 0, 2

books = {
    "Book 1": 10,
    "Book 2": 15,
    "Book 3": 20,
    "Book 4": 25,
    "Book 5": 30,
    "Book 6": 35,
    "Book 7": 40,
    "Book 8": 45,
    "Book 9": 50,
    "Book 10": 55
}


total_price = sum(books.values())

total_price_5_discount = total_price * (0.9 if len(books) >= 5 else 1)
total_price_10_discount = total_price * (0.8 if len(books) >= 10 else 1)

print("ფასი ფასდაკლების გარეშე:", total_price)
print("ფასი 10% ფასდაკლებით 5 წიგნზე:", total_price_5_discount)
print("ფასი 20% ფასდაკლებით დანარჩენ 5 წიგნზე:", total_price_10_discount)


# print(10 + 15 + 20 + 25 + 30 + 35 + 40 + 45 + 50 + 55)
print(325 * 0.9)
print(292.5 * 0.8)
