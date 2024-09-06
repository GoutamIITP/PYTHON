'''Write a program to check wheather a character is aplphabet digit or special character'''

ch = input("Enter the string")
for i in ch:
    if i.isalpha():
        print(i,"is an aplabet")
    elif i.isdigit():
        print(i,"is an digit")
    else:
        print(i,"is an special character")

