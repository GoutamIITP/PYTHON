def recommend_food(species, age):
    if species.lower() == "dog":
        if age < 2 :
            print("Give puppy food")
        elif age >=2 and age < 7:
            print("Give adult dog food ")
        else:
            print("Give senior dog food")

    elif species.lower() == "cat":
        if age < 5 :
            print("Give junior cat food")
        elif age >=5 and age < 7:
            print( "Adult cat  Food")
        else:
            print("Give senior cat food")
    else:
        print("No other  species for recommendation")

pet_species = input("Enter the species (cat/dog): ")
pet_age = int(input("Enter the age: "))

recommend = recommend_food(pet_species, pet_age)


