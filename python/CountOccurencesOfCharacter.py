# count the occurrence of a given character in a string

import re

inputStr = "saisgit"
print(len(re.findall('s', inputStr)))


def check_count(s, char):
    count = 0
    for i in s:
        if i == char:
            count = count + 1
    return count


print(check_count("saisgit", 's'))
