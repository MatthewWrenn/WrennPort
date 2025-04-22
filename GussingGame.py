#this is my gussing game maybe you'll guess right?!
import random
#takes users name checks that is is alhpa for validation reasons.
print("Greetings and salutations! I am P-4Y0 human cyboorg relations.")
while True:
    Name = input("Might I have your name? ").strip()
    if Name.replace(" ", "").isalpha():
        break
    print("Excuse me! I am programmed to accept only letters at this point.")
#user gets 6 guesses at the number. Also validates the input to be expect ints.
num = random.randint(1, 100)
print(f"Please {Name}, I implore you to take a guess at a number between 1 and 100. You regrettably are only allowed 6 chances, do use them wisely.")
for guessesTaken in range(1, 7):
    while True:
        try:
            guess = int(input("Might I have your guess? "))
            if guess >= 0:
                break  # Exit the input loop if the guess is valid
            else:
                print("Excuse me! I am programmed to accept only positive whole numbers at this point.")
        except ValueError:
            print("Excuse me! I am programmed to accept only whole numbers at this point.")
    if guess < num:
        print("I'm sorry, I regret to inform you have guessed to low.")
    elif guess > num:
        print("I'm sorry, I regret to inform you have guessed to high.")
    else:
        break
if guess == num:
    print(f"Congratulations {Name}! You guessed the number {num} in {guessesTaken} guesses! Wonderful!")
else:
    print(f"{Name}! I regret to inform, the number was {num}. Pehaps you will have better luck next time?")


   