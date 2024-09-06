string = "teeterpacacded"

for char in string:
    print(char)
    if string.count(char) == 1:
        print("Char is :", char)
        break

