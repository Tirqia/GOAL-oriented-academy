family = ["nato", "edemi", "aleko", "beqa"]
ages = [50, 55, 15, 22]

ages_in_10_years = [age + 10 for age in ages]

name = "My mom's name is: {},My father's name is: {}, My brother's name is: {}, My name is: {}".format(family[0], family[1], family[3], family[2])
age_10_years_later = "We are {} years old, and in 10 years, we will be {} years old.".format(
([str(age) for age in ages]),
([str(age) for age in ages_in_10_years])
)

print(name)
print(age_10_years_later)   #პასუხი-#My mom's name is: nato,My father's name is: edemi, My brother's name is: beqa, My name is: aleko
# We are ['50', '55', '15', '22'] years old, and in 10 years, we will be ['60', '65', '25', '32'] years old.

