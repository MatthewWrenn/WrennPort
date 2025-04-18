# This will say hello and ask for your name and REJECT non-alphabetical characters
print("Ello' Guv")
while True:
  myName = input("Wot's your name? ")
  if myName.replace(" ", "").isalpha():
    break
  print("Oi mate, letters only!")
print("Innit just a great name though, " + myName)
print("Just the right number of leters at")
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
    print("Oi you gettin' cheeky wiv me guv? Numbas only!")

print("Incorrect a Woodchuck can chuck" + str(round(chuckedwood + 3, 2)) +
      " chucks of wood!")
