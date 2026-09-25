"""Merge two lists and return all their values in sorted order."""


def sorted_list():
    list1 = [4, 3, 7, 3, 7, 28, 2, 89]
    list2 = [1, 2, 3, 4, 5, 43, 21]
    list1.sort()
    merge_list = sorted(list1 + list2)
    return merge_list


print(sorted_list())
