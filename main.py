# This will say hello and ask for your name and REJECT non-alphabetical characters
print("Greeting and salutations!")
while True:
  myName = input("Might I have your name?")
  if myName.replace(" ", "").isalpha():
    break
  print("Excuse me! I am programmed to accept only letters at this point.")
print("Ahhh, what wonderful name " + myName)
print("Just the right number of leters")
print(len(myName))
#This is a is meant as a joke and will add 3 to the number you input also will REJECT non-numerical characters. Accepts floats though :D
while True:
  try:
    chuckedwood = float(
        input(
            "How much wood could a woodchuck chuck if a wood chuck could chuck wood? "
        ))
    break
  except ValueError:
    print("Excuse me! I am programmed to accept only numbers at this point.")

print("Incorrect a Woodchuck can chuck" + str(round(chuckedwood + 3, 2)) +
      " chucks of wood!")
