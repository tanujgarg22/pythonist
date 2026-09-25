"""Reverse a list manually by assigning values to reverse indexes."""


def reverse_list():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = list1.copy()
    length = len(list1)
    for index, item in enumerate(list1):
        reverse_index = (length - 1) - index
        print(
            f"index is {reverse_index} list2[{reverse_index}] is "
            f"{list2[reverse_index]} and list1[{index}] is {item}"
        )
        list2[reverse_index] = item

    return list2


print(reverse_list())
