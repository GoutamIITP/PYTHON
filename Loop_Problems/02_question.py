age = int(input("Enter the  age: "))
day = input("Enter the day: ")

price = 12 if age >= 18 else 8

if day.lower() == "wednesday":
    price -= 2

print("ticket price in $",price)