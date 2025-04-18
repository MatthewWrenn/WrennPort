# Asks the user for a name and rejects non-alphabetical characters
print("Greetings and salutations!")
while True:
    myName = input("Might I have your name? ")
    if myName.replace(" ", "").isalpha():
        break
    print("Excuse me! I am programmed to accept only letters at this point.")

print(f"Ahhh, what a wonderful name {myName}")
print(f"It has {len(myName)} letters - just perfect!")

# Woodchuck question - accepts only numbers and adds 3 to the response also rounds to 2 decimal places.
while True:
    try:
        chuckedwood = float(input("How much wood could a woodchuck chuck if a woodchuck could chuck wood? "))
        break
    except ValueError:
        print("Excuse me! I am programmed to accept only numbers at this point.")

print(f"Incorrect! A woodchuck can {round(chuckedwood + 3, 2)} chucks of wood!")
