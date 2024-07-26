def find_short(s):
    words = s.split()
    shortest_length = len(words[0])
    for word in words:
        if len(word) < shortest_length:
            shortest_length = len(word)
    return shortest_length


print(find_short("Lets all go on holiday somewhere very cold"))


def find_short(s):
    return min(len(x) for x in s.split())


print(find_short("Lets all go on holiday somewhere very cold"))
