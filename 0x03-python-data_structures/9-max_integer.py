
#!/usr/bin/python3
# 9-max_integer.py
# Ifeanyi I Ekezie
def max_integer(my_list=[]):
    # Initialize the max value to None
    max_value = None
    for num in my_list:
        if max_value is None or num > max_value:
            max_value = num
    return max_value
