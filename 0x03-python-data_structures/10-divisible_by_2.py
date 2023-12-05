#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    counter = 0
    list_result = my_list[:]
    for i in copy_list:
        # Check if the element is divisible by 2
        if i % 2 is 0:
            # Append True to the result list
            list_result[counter] = True
        else:
            # Append False to the result list
            list_result[counter] = False
        counter = counter + 1
    # Return the result list
    return list_result
