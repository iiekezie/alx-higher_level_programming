def delete_at(my_list=[], idx=0):
    # check if the index is valid
    if 0 <= idx < len(my_list):
        # loop through the list and copy the elements except the one at idx
        new_list = []
        for i in range(len(my_list)):
            if i != idx:
                new_list.append(my_list[i])
        # return the new list
        return new_list
    # if the index is invalid, return the original list
    else:
        return my_list

