'''Create a function with a default arguments'''

def show_employee(name, salary = 9000):
    print(f"name: {name} salary: {salary}")

show_employee("Ben", 1200)
show_employee("jesy")