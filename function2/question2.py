'''Write a user defined function to check whether the string is palindrome or not'''

def isplaindrome(s, start, end):
    if start >= end:
        return 1
    if s[start] !=  s[end]:
        return 0
    return isplaindrome(s, start + 1, end - 1)

b = input("Enter the string:")
res = isplaindrome(b , 0, len(b) - 1)
if res == 1:
    print("The the string is plaindrome")
else:
    print("It is not palindrome")


#  cheeck string is palindrome using flag
