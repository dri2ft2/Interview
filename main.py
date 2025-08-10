# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# [1,2,3,4,5,5,5,5,0 -3] - > True
# [1,2,3,4,5,6,7] -> False
# [0] -> False 0 - IGNORE
# [0, 3, 4, -3] -> True

# def has_opposite(lst: list[int]) -> bool:
#     non_duplicates_set = set(lst)
#     for num in non_duplicates_set:
#         if -num in non_duplicates_set and num != 0:
#             return True
#     return False
#

# [1,2,3,4,5,6] -> False
# [2,3,5, 1, 4] -> 2
# [9, 3, 12, 6, 6] -> 2
# [9,1,2,3,4,5] - False

# def get_sum_index(lst: list[int]) -> int:
#     for index, number in enumerate(lst):
#         left_sum = sum(lst[:index])
#         right_sum = sum(lst[index + 1:])
#         if left_sum == number == right_sum:
#             print(index)
#     print(False)
#
#
# get_sum_index([1,2,3,4,5,6])
# get_sum_index([2,3,5, 1, 4])
# get_sum_index([9, 3, 12, 6, 6])
# get_sum_index([9,1,2,3,4,5])
#
#
# print(has_opposite([1,2,3,4,5,5,5,5,0 -3]))
# print(has_opposite([1,2,3,4,5,6,7]))
# print(has_opposite([0]))
# print(has_opposite([0, 3, 4, -3]))
from itertools import zip_longest

str_1, str_2 = "catcat" , "dog"

# [('c', 'd'), ('a', 'o'), ('t', 'g'), ('A' ,'d')]

def pikachu_lol(kebab):
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
# HELLO