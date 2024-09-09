#!usr/bin/python3
def uniq_add(my_list=[]):
    integers = set()
    for number in my_list:
        integers.add(number)
    return sum(integers)
