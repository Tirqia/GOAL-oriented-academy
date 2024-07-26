"""
    Find the first number of a sequence if present in a string, otherwise return the string as an integer.

    Algorithm: Attempt to recreate the string by consecutively adding numbers in sequence until the newly created
               string is at least as long as the given string `s`. If the newly created string is equal to the 
               given string, return the first number in the sequence. Begin each sequence by choosing the first
               n digits of the string (up to half the string length) starting from 1, since the minimum starting
               number is desired. If no matching string can be made, return the original string as an integer.
"""


def find(s):
    n = len(s)

    for length in range(1, n // 2 + 1):
        first_number = int(s[:length])
        current_number = first_number
        sequence = str(current_number)

        while len(sequence) < n:
            current_number += 1
            sequence += str(current_number)

        if sequence == s:
            return first_number
    return int(s)


print(find("9899100"))
