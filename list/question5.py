'''Input String list, write a python program to filter all the string,
Which have a smilar case, either upper or lower'''

lst = input("Enter the stirng: \n").split()

def fiter_string(string_lst):
    upper_case_strings = [word for word in string_lst if word.isupper()]
    lower_case = [word for word in string_lst if word.islower()]
    return upper_case_strings + lower_case

    
result = fiter_string(lst)

print("The filtered strings are: " + ' '.join(result))