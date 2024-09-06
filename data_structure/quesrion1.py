# Input two sets, 'set1' & 'set2' and do the following.abs
# union12
# intersection
# Difference

set1 = set(input("Enter the numer").split(" "))
set2 = set(input("Enter the numer").split(" "))

a = set1.union(set2)
print(a)
i = set1.intersection(set2)
print(i)
z = set1.difference(set2)
print(z)