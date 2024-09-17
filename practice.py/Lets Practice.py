print("We have the age special. Where kids under 13 eat free, adults pay regular price which is $15 per plate and seniors get 50% percent off!")

name = input("What is your name? ")
age = float(input("Hi " + name + ", how old are you? "))
food = 15.00



if age <= 13:
    food = age * 0
    print("Kids eat free!")
elif age >= 14 and age <= 49:
    print(f"Alright {name}, your total comes out to ${food}")
else:
    food = 15 / 2 
    print(f"Alright s{name}, your total comes out to ${food}")