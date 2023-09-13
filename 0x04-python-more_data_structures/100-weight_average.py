#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    sum = 0
    product = 0

    for sub in my_list:
        product += sub[0] * sub[1]
        sum += sub[1]
    res = product / sum

    return res
