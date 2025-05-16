"""
 A functions that sort the list
"""


def list_sorter(input_list: list) -> list:
    return sorted(input_list)


# def remove_duplicates(input_list: list) -> list:
#     set_list = list(set(input_list))
#     # print(set_list)
#     return set_list

# def remove_duplicates(input_list: list) -> list:
#     set_list = set()
#     for item in input_list:
#         if item not in set_list:
#             set_list.add(item)
#
#     return list(set_list)

def remove_duplicates(input_list: list) -> list:
    seen = set()
    seen = [x for x in input_list if not (x in seen or seen.add(x))]
    return sorted(seen)


# print(remove_duplicates([1, 5, 5, 3, 5, 2, 3, 2, 3, 1, 7, 9, 4, 6]))
# print(remove_duplicates([4, 3, 1, 7, 6, 2, 9, 3, 2, 1, 2]))
