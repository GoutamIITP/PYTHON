import math
def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle(4)

a = round(a, 2)
c = round(c, 2)

print("Area: ",a,"circumference: ", c)