'''write a user defined function to remove 1th chracter from string '''

def remove(i,s):
    a = s[:1]
    b = s[i+1:]
    return a + b

n = input("Enter the string: ")
b = int(input("Enter the postion where you wanna remove: "))

# Ensure the position is valid
if 0 <= b < len(n):
    res = remove(b, n)
    print("Resulting string:", res)
else:
    print("Invalid position")