'''
Instructions to run the program:
    In the command prompt, type:
        python Shilong_Zhao_hw1.py
    (Before running, check if the current directory contains Shilong_Zhao_hw1.py)
'''

def isLeap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


if(isLeap(1000)):
    print("1000 is a leap year")
else:
    print("1000 is not a leap year")

