while True:
    age = (input("Enter the age: "))

    if age.lower() == 'quit':
        break
    
    age = int(age)

    if age < 13:
        print("he/she is a child")
    elif age < 20:
        print("He/She is a teenager")
    elif age < 60:
        print("He/She is Adult")
    else:
        print("He/She is a senior")