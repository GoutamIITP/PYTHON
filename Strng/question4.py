'''Write a program to check if two string Anagram or not '''

s1 = input("Enter the string: ")
s2 = input("Enter the string: ")

if sorted(s1) == sorted(s2):
    print("It is Anagram")
else:
    print("It is not Anagram")