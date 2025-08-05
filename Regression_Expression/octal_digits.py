'''Problem Statement:
Write a Python program that checks whether each number in a given list of strings contains only octal digits (digits from 0 to 7).
Use regular expressions to validate each string and print whether it is a valid octal number or invalid'''
import re
string=['789','123','004']
pattern=r'^[0-7]+$'

for s in string:
    if re.search(pattern,s):
        print(f"{s} = Vaild Octal")
    else:
        print(f"{s} = Invalid Octal")    
