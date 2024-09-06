size = input("Order  of coffe (small/ medium/large)".lower())
extra_shot = input("If you want extrashot.(yes/NO)".lower())

if size == {'small', 'large', 'medium'}:
    print(f"the order is {size}")
elif extra_shot == "yes":
    print(f"the order is {size} with extra shot")
elif extra_shot  == "no":
    print(f"The only order is {size}")