# homework6

"""homework 6."""


def hw6_repl():
    """Replace '#'"""
    my_str = "www.my_site.com#about"
    str_new = my_str.replace("#", "/", 1)
    return str_new


def hw6_add_ing(word):
    """Add 'ing'"""
    return word + "ing"


def hw6_swap_str():
    """Swap first and last name"""
    my_str = "Ivanou Ivan"
    my_list = my_str.split()
    result = ' '.join(my_list)
    return result


def hw6_remove_whitespace(text):
    """Remove whitespace"""
    return ' '.join(text.split())


def hw6_fix_name(name):
    """Capitalize"""
    return name.capitalize()


def hw6_str_to_list(word):
    """Split a string"""
    return word.split()


def hw6_format_greeting(names, greeting, place):
    """Return a greeting"""
    name = names[0]
    return f"Hello, {name}! {greeting} to {place}"


def hw6_list_to_string(lst):
    """Convert a list"""
    return ' '.join(lst)


def process_list(lst, new_value):
    """Insert new value"""
    lst.insert(2, new_value)
    del lst[6]
    return lst
