mother_age = 50
father_age = 56
brother_age = 23

later = {
    father_age + 25,
    mother_age + 25,
    brother_age + 25
}

print(later)

mother_age = 50
father_age = 56
brother_age = 23

later = mother_age + 25
later1 = father_age + 25
later2 = brother_age + 25

print(
    f"Mother's age after 25 years {later}: father's age after 25 years {later1}: brother's age after 25 years {later2} ")


mother_age = int(input("Enter your mother's age: "))
father_age = int(input("Enter your father's age: "))
brother_age = int(input("Enter your brother's age: "))

mother_future_age = mother_age + 25
father_future_age = father_age + 25
brother_future_age = brother_age + 25

print(
    f"After 25 years, your mother will be {mother_future_age} years old, your father will be {father_future_age} years old, and your brother will be {brother_future_age} years old.")
