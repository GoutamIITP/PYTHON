''' write a program to check whether a given number is an armstrong number or not '''


def check_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_digits = sum(int(i) ** num_len for i in num_str)
    return sum_of_digits == num

num = int(input("Enter the number: "))
if check_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")