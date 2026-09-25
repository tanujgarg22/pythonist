"""Check for duplicates and return immediately when one is found."""


def check_dup_fast_exit():
    list1 = [1, 2, 2, 3, 4, 5, 6]
    list2 = []
    for item in list1:
        if item in list2:
            return True
        list2.append(item)
    return False


print(check_dup_fast_exit())
