def age_difference(ages):
    youngest = min(ages)
    oldest = max(ages)
    difference = oldest - youngest
    return (youngest, oldest, difference)


family_ages = [34, 55, 12, 67, 22, 4, 78, 0]
result = age_difference(family_ages)
print(result)

# 2
family_ages = [34, 55, 12, 67, 22, 4, 78, 0]

youngest = family_ages[0]
oldest = family_ages[0]

for age in family_ages:
    if age < youngest:
        youngest = age
    if age > oldest:
        oldest = age

difference = oldest - youngest

result = (youngest, oldest, difference)

print(result)
