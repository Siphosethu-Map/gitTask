country = input("Which country are you from?: ")

print(country)

print("_________________________________________________________________")

# this is a full name user request
# then enter their name and a message is printed
print("You are required to enter your full name!\n")

full_name = input("Please enter your full name: ")

if len(full_name) > 1 and len(full_name) < 4:
    print("""That surely can't be your full name.\n""")
elif len(full_name) > 5 and len(full_name) < 25:
    print("Thank you for entering your full name.\n")
elif len(full_name) == 0:
    print("You haven't entered anything. Please enter your name.\n")
elif len(full_name) > 25:
    print("""You have entered more than 25 characters. Please make sure that
           you have only entered your full name.\n""")
else:
    print("Invalid entry")

print("_________________________________________________________________")

# This is a bmi calculator.
# The user will enter their weight and height, then the bmi will be calculated
# using the  formula below.
# the answer will be put in a loop that will give us the results, being the
# BMI category the user is in.

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
