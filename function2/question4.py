'''Write a recursive function to reverse an integer.'''

# n = 4562
# rev_num = 0
# while(n > 0):
#     a = n % 10
#     rev_num = rev_num*10 + a
#     n = n // 10

# print(rev_num)

# Recursive approach 

def rev(n, s):
    if (n != 0):
        a = n % 10
        s = s*10 + a
        return rev((n // 10), s)
    else:
        print("Reverse: ",s)


n = int(input("Enter the number: "))
rev(n, 0)