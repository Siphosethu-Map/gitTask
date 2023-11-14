country = input("Which country are you from?: ")

print(country)

print("_________________________________________________________________")

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
