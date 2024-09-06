password = input("Enter the password:  ")

if len(password) < 6:
    strength  = "Weak"
elif len(password) <= 10:
    strength = "mediam"
else:
    strength = "strong"

print(strength)