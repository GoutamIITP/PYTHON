marks = int(input("Enter the marks: "))

if  marks >= 101:
    print("Re- Enter the marks")
    exit()
if marks >= 90:
    print("Stundet are in A postion")
elif marks >=80:
    print("student are in B postion")
elif marks >=70:
    print("student are in C position")
elif marks >= 60:
    print("student are in D postion")
else :
    print("Student are in F position")

    

print(f"Student have obtain {marks} Marks ")