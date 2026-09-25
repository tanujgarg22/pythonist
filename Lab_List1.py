"""Calculate the sum of all numbers and integers in a mixed list."""


def sum_list():
    list1 = [1, 2, 3, 4, 5, -6]
    total = sum(list1)
    return total


def sum_mixedlist():
    list1 = [1, 2, 3, "apple", 4, "cat", 60]
    total = sum(element for element in list1 if isinstance(element, int))
    return total


print(sum_list())
print(sum_mixedlist())
