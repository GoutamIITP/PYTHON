'''write a program to print element with maximum vowels from a list'''

test_list = input("Enter the string: \n").split()

print("Original list: " + str(test_list))

res =  ""
max_len = 0

for i in test_list:
    vowel_len = len([a for a in i if a in ['a','e','i','o','u','A','E','I','O','U']])

    if vowel_len > max_len:
        max_len = vowel_len
        res = i

print("Maximum vowels word: " + str(res))