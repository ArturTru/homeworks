# homework8

"""homework 8"""

import random


def rand4():
    '''random function for all'''
    first = random.choice(range(1, 10))
    rest = random.sample([d for d in range(10) if d != first], 3)
    return int(''.join(map(str, [first] + rest)))


def hw8_cow_bull(a: int):
    '''cow bull'''
    b = rand4()
    a_list = list(str(a))
    b_list = list(str(b))


    def count(a_list, b_list):
        '''count function'''
        cows = 0
        bulls = 0
        for i, a_digit in enumerate(a_list):
            for j, b_digit in enumerate(b_list):
                if a_digit == b_digit:
                    if i == j:
                        bulls += 1
                    else:
                        cows += 1
                    break
        return cows, bulls
    return count(a_list, b_list)


def hw8_2(a, b):
    '''two hm'''
    if a == b:
        return False
    if a > b:
        return True
    return (b - a) % 2 != 0


def hw8_statues(statues):
    '''ststues'''
    if not statues:
        return 0
    arr = statues.copy()
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    missing = 0
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff > 1:
            missing += diff - 1

    return missing