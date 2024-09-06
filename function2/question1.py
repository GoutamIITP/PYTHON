'''write two user defined function to calculate HCF and LCM of two numbers'''

def hcf(a,b):
    if (b == 0):
        return a
    if (a == 0):
        return b
    return hcf(b, a % b)
 

def lcm(a,b):
    return (a * b) // hcf(a,b)
num =  input("Enter the number: ")
a, b = map(int, num.split())
if a < b:
    a , b = b , a
else: 
    a, b

print("Lcm: ", lcm(a,b))
print("hcf: ",hcf(a,b))

