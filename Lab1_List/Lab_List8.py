"""Find the maximum absolute difference between consecutive list elements."""


def bruteforce():
    list1 = [10, 20, 40, 50000, 90, 100, 450, 890, 1, 4]
    difference = 0
    for index in range(len(list1) - 1):
        value_difference = abs(list1[index] - list1[index + 1])
        print(f"value_x is list1[{index}] and value_y is list1[{index + 1}]")
        if value_difference > difference:
            difference = value_difference

    return difference


print(bruteforce())
