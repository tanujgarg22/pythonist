"""Rotate a list so that the selected key becomes the first element."""


def circular_list():
    list1 = [1, 2, 3, 4, 5]
    key = 3

    def reverse_list(list_to_reverse, start, end):
        while start < end:
            list_to_reverse[start], list_to_reverse[end] = (
                list_to_reverse[end],
                list_to_reverse[start],
            )
            start += 1
            end -= 1
        return list_to_reverse

    result = reverse_list(list1, 0, len(list1) - 1)
    reverse_list(result, 0, key - 1)
    reverse_list(result, key, len(list1) - 1)
    return result


print(circular_list())
