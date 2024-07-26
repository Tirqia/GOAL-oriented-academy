def get_sum(a, b):
    if a == b:
        return a

    if a > b:
        a, b = b, a

    total_sum = 0
    for num in range(a, b + 1):
        total_sum += num

    return total_sum


print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))
