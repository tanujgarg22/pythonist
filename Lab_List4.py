"""Check whether a list contains duplicate values."""


def check_dup():
    list1 = [1, 2, 3, 4]
    list2 = []
    for item in list1:
        if item not in list2:
            list2.append(item)

    if len(list2) < len(list1):
        print("duplicate in original list")
        return True

    print("no dups")
    return False


print(check_dup())
