distance  =  int(input("Enter the distance: "))

if distance <3:
    suggest = "walk"
elif distance <= 15 :
    suggest = "Bike"
else:
    suggest = "Car"

print(suggest)
