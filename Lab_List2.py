"""Find the largest integer in a list that may contain other data types."""


def find_largest():
    list1 = [4555, "Tanuj", 678, 45677, "hello", 24526, "hi", 64, 6]
    max_num = max(element for element in list1 if isinstance(element, int))
    return max_num


print(find_largest())
