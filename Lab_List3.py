"""Remove duplicate values from a list while preserving their order."""


def remove_dups():
    list1 = [1, 22, 22, 33, 44, 33, 5, 6, 9, 9]
    unique_list = []
    for item in list1:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


print(remove_dups())
