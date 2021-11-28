# Check whether string contains only numbers or not

import re


def check_numbers(s):
    if re.match('^[0-9]*$', s):
        print("String contains all numbers")
    else:
        print("String doesn't contain all numbers")


string1 = '1234556'
string2 = 'ab123bc'
check_numbers(string1)


def check_numbers2(s):
    try:
        num = int(s)
        print("String1 contains only digits")
    except:
        print("String1 doesn't contains only digits")


check_numbers2(string2)