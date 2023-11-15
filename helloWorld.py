country = input("Which country are you from?: ")

print(country)

print("_________________________________________________________________")


# This is the use full name section
# user is required to input their Full name
# after that a message will
print("\nYou are required to enter your full name!\n")

full_name = input("Please enter your full name: ")

if len(full_name) > 1 and len(full_name) < 4:
    print("""That surely can't be your full name.\n""")
elif len(full_name) > 5 and len(full_name) < 30:
    print("Thank you for entering your full name.\n")
elif len(full_name) == 0:
    print("You haven't entered anything. Please enter your name.\n")
elif len(full_name) > 30:
    print("""You must really have a really long name. Please make sure that
           you have only entered your full name.\n""")
else:
    print("Invalid entry")

print("_________________________________________________________________")

# This is a bmi calculator.
# The user will enter their weight and height, then the bmi will be calculated
# using the  formula below.
# the answer will be put in a loop that will give us the results, being the
# BMI category the user is in.
print("This is a B.M.i calculator")
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))

bmi = weight / (height)**2
print(f"\nYour BMI index is {bmi}: ")

if bmi >= 30:
    print("You are obese.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal.")
else:
    print("You are underweight.")

print("______________________________________________________________")
