# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if name == 'main':
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

def get_tuples(str1, str2):
    letter_list = []
    longer_sting = str1 if len(str1) > len(str2) else str2
    is_longer_str1 = longer_sting == str1
    for i in range(len(longer_sting)):
        try:
            letter_tuple = (str1[i], str2[i])
            letter_list.append(letter_tuple)
        except IndexError:
            if is_longer_str1:
                letter_tuple = (longer_sting[i], "A")
            else:
                letter_tuple = ("A", longer_sting[i])
            letter_list.append(letter_tuple)
    return letter_list


print(get_tuples(str_1, str_2))