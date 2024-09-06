'''find the length of any given word in a string
'''
n = input("Enter the string: ")
print("Original string: ", n)
wrd = input("Enter the word: ")
x = n.split()
print(x[1])
if wrd in x:
    print(f"The length of the word'  {wrd} is: {len(wrd)}")
    res = x.index(wrd) + 1
    print("The location of word is: ", res)
else:
    print(F"The word {wrd} is not found in string")