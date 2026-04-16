# Ex
"""ex_1"""

def process_string():
    while True:
        s = input("input ")
        if len(s) >= 15:
            break
        print("Error")

    print(s)
    s = s[1:]
    print(s)
    s = s[:-1]
    print(s)
    print(s[2])
    print(s[-3])
    print(len(s))
    s = s[::-1]
    print(s)
    s = s[8:]
    print(s)

"""ex_2"""

def print_sq():
    while True:
        try:
            n = int(input("input a number: "))
            print(f"sq{n} = {n ** 2}")
            break
        except ValueError:
            print("Error")

def check():
    while True:
        try:
            x = int(input("input a number: "))
            print("True" if x % 2 == 0 else "False")
            break
        except ValueError:
            print("Error")

"""ex_3"""

def sum_n():
    while True:
        try:
            n = int(input("input N: "))
            if n < 1:
                print("Error. expect > 0")
                continue
            total = n * (n + 1) // 2
            print(f"Sum {n} = {total}")
            break
        except ValueError:
            print("Error")

"""ex_4"""

def plus_one():
    while True:
        my_input = input("dig. sep. by comma\space: ")
        try:
            part = my_input.replace(',', ' ').split()
            lst = [int(i) for i in part]
            numb = int(''.join(str(d) for d in lst))
            numb += 1
            result = [int(d) for d in str(numb)]
            print(result)
            break
        except ValueError:
            print("Error")

"""ex_5"""


def is_pol():
    while True:
        try:
            num = int(input("Input number: "))
            break
        except ValueError:
            print("Error")

    if num < 0:
        print("FALSE")
    else:
        s = str(num)
        print("TRUE" if s == s[::-1] else "FALSE")

"""ex_6"""

def file_stats(g):
    c = open(g).read()
    l = c.count('\n') + 1 if c else 0
    w = len(c.split())
    let = sum(1 for x in c if x.isalpha())
    s = "\nLines: " + str(l) + "\nWords: " + str(w) + "\nLetters: " + str(let)
    print(s)
    open(g, 'a').write(s)


"""ex_7"""

def f():
    s = input("string: ")
    while True:
        try:
            n = int(input("number: "))
            if n < 0:
                print("Error")
                continue
            break
        except ValueError:
            print("Error")

    part = s[:n]
    result = part + part[-2::-1]
    print(result)

"""ex_8"""



"""ex_9"""



"""ex_10"""

def decorator(*d_args, **d_kwargs):
    decorator1 = d_args
    decorator2 = d_kwargs

    def inner(func):
        def wrapper(x):
            print((decorator1, decorator2))
            result = func(x)
            return result
        return wrapper
    return inner