s = input("Enter the string: ")
print(s[:len(s) // 2].upper() + s[len(s) // 2:].lower())