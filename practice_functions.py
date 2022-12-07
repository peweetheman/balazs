
# Given a list and element, return the index of the element in the list

# ONE EXAMPLE:
# list = [9124, 213, 213, 53, 78, 2]
# element = 78
# GOAL: return 4
from typing import List


def fun(list, element):
    return 3

def findIndex(list, element):
    for i in range(len(list)):  #range(n) -> [0, 1, 2, 3,..., n-1]
        if list[i] == element:
            return i
    return False # if we reach the end of the for loop, none of the elements matched


# Find the two indices of element1 and element 2
# ONE EXAMPLE:
# list = [9124, 213, 213, 53, 78, 2]
# element1 = 78, element2 = 2
# GOAL: return (4, 5)
def findTwoIndices(list, element1, element2):
    output = (False, False)
    list_len = len(list)
    range_list = range(len(list))
    for i in range(len(list)):
        if element1 == list[i]:
            output = (i, output[1])
        if element2 == list[i]:
            output = (output[0], i)
    return output


# Given a list and element, return the index of the element in the list

# ONE EXAMPLE:
# list = ["hello world", "sadf", "ytre", "asdfa", "bob", "alice", "balazs"]
# element = "bob"
# GOAL: return 4
def findIndex(list: List[str], element: str):
    for i in range(len(list)):
        if list[i] == element:
            return i
    return


# check if a number x is a palindrome
# Palindrome: A number that is the same backwards and forwards  5-3-1-3-5
# (e.g. 998899 is a palindrome, 121 is a palindrome, 54345 is a palindrome)
# 09842

# 9987542---2437899
# 98422 22489  <- x[0] = 9, x[1] = 8
# 32123 yes still palindrome
def isPalindrome(x: int):
    x = str(x)
    middle_index = len(x) / 2
    print(x[0])
    print(x[1])
    if x[0:middle_index] == reversed(x[middle_index:-1]):
        print("it's a palindrome")
    else:
        print("it's not a palindrome")

    # or check one by one
    for i in range(len(x)):
        if x[i] != x[-i]:
            print("it's not a palindrome")


isPalindrome(998899)



# print(len([143209480248042398348, 4, 52, 512, 24])) # is 5
# findIndex(["hello world", "sadf", "ytre", "asdfa", "bob", "alice", "balazs"], "bob")






#
# def minimum(list):
#     # return the smallest element in the list
#     smallest_seen = 1000000000000
#     for i in list:
#         if i < smallest_seen:
#             smallest_seen = i
#     return smallest_seen
#
# def sort(list):
#     # return a sorted list in increasing order
#     sorted_list = []
#
#     while len(list) > 0:
#         smallest_element = minimum(list)
#         sorted_list.append(smallest_element)
#         list.remove(smallest_element)
#
#     return sorted_list
#
# print(sort(list=[5, 2, 4, 3, 7, 9]))  # should return [2,3,4,5,7,9]
# print(sort(list=[92340820943, 3249082093480, 324082093482, 29048209, 932482904820, 23490820948, 23490823904]))
