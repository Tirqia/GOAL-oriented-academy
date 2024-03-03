age = int(input("asaki"))
limit = 20
height = int(input("simagle"))
if age > limit or height > 200:
    print("მაღალი ხარ")
elif age < limit or height > 200:
    print("მაღლიხარ მაგრამ პატარა")
else:
    print("დაბალი ხარ")