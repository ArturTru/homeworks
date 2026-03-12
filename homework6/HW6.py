def hw6_repl ():
    my_str = "www.my_site.com#about"
    str_new = my_str.replace("#","/", 1)
    return str_new

def hw6_add_ing (word):
    return word + "ing"

def hw6_swap_str ():
    my_str = "Ivanou Ivan"
    my_list = my_str.split()
    result = ' '.join(my_list)
    return result

def hw6_remove_whitespace(text):
    return ' '.join(text.split())

def hw6_fix_name(name):
    return name.capitalize()

def hw6_str_to_list (word):
    return word.split()

def hw6_format_greeting(names, greeting, place):
    name = names[0]
    return f"Hello, {name}! {greeting} to {place}"

def hw6_list_to_string(lst):
    return ' '.join(lst)

def process_list(lst, new_value):
    lst.insert(2, new_value)
    del lst[6]
    return lst







