#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    counter = 0
    list_result = my_list[:]
    for i in copy_list:
        # Check if the element is divisible by 2
        if i % 2 is 0:
            list_result[counter] = True
        else:
            list_result[counter] = False
        counter = counter + 1
    return list_result
