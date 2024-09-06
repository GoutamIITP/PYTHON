'''  write a program that generate a list of 20 random numbers between ,
     1 and 100. Remove the first and last item from the list,
     sort thr remaining item and print the result.abs'''

import random as r
print(sorted(r.randint(1, 100) for i in range(0,20)[1:19]))