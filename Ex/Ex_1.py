"""
Module for exam tasks.
"""

def process_string():
    """Process a string of at least 15 characters as required."""
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


def print_sq():
    """Ask for a number and print its square."""
    while True:
        try:
            n = int(input("input a number: "))
            print(f"sq{n} = {n ** 2}")
            break
        except ValueError:
            print("Error")


def check():
    """Ask for a number and print whether it is even."""
    while True:
        try:
            x = int(input("input a number: "))
            print("True" if x % 2 == 0 else "False")
            break
        except ValueError:
            print("Error")


def sum_n():
    """Calculate sum from 1 to N using formula."""
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


def plus_one():
    """Take a list of digits, increment by 1, return as list."""
    while True:
        my_input = input("dig. sep. by comma\\space: ")
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


def is_pol():
    """Check if input number is palindrome."""
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


def file_stats(g):
    """Count lines, words, letters in a file and append results."""
    with open(g, 'r', encoding='utf-8') as f:
        c = f.read()
    lines = c.count('\n') + 1 if c else 0
    words = len(c.split())
    letters = sum(1 for x in c if x.isalpha())
    s = "\nLines: " + str(lines) + "\nWords: " + str(words) + "\nLetters: " + str(letters)
    print(s)
    with open(g, 'a', encoding='utf-8') as f:
        f.write(s)


def f():
    """Create string from first n chars plus mirror."""
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


def decorator(*d_args, **d_kwargs):
    """Decorator with parameters that prints its arguments."""
    decorator1 = d_args
    decorator2 = d_kwargs

    def inner(func):
        def wrapper(x):
            print((decorator1, decorator2))
            result = func(x)
            return result
        return wrapper
    return inner