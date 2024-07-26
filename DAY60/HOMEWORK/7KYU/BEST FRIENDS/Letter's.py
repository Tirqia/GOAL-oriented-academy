def best_friend(txt, a, b):
    words = txt.split()
    for word in words:
        found_a = False
        for i in range(len(word) - 1):
            if word[i] == a and word[i + 1] == b:
                found_a = True
                break
        if not found_a:
            return False
    return True


print(best_friend("he headed to the store", "h", "e"))
print(best_friend("abcdee", "e", "e"))
print(best_friend("i found an ounce with my hound", "o", "u"))
print(best_friend("we found your dynamite", "d", "y"))
