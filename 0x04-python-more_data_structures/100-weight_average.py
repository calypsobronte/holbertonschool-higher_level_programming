#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num1 = 0
    num2 = 0
    temp = 0
    for num in range(len(my_list)):
        num1 += my_list[num][0] * my_list[num][1]
        num2 += my_list[num][1]
    return num1 / num2
