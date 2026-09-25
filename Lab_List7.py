"""Count even and odd numbers and return both counts in a tuple."""


def count_evenodd():
    list1 = [2, 4, 6, 8, 3, 5, 7, 9, 22, 44, 55]
    count_even = 0
    count_odd = 0

    for item in list1:
        if item % 2:
            count_odd += 1
        else:
            count_even += 1

    return count_even, count_odd


print(count_evenodd())
