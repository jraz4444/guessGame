#Greets the user and tell the user how many guesses they have.
print("Hi.  How are you? ")
# Generate a random number within  a 20 number range
from random import *
randNum = randint(1,20)
#print(randNum)
#limit the number of guesses
count =1
numGuesses = 1
#Tell the user how many guess they are allowed.
print("You are allowed ten guess.")
#Tell the user to guess the number within the range
print("You can only enter a number that is within the range of 1 to 20. ")
#Ask for a number
guess = int(input("Guess a number between 1 and 20: "))
  #Guess the number within the range and tell the user
  #correct answer when they reach their limit on guesses.
while guess != randNum and count <= 10:
    if guess < 1:
        print("You have guessed outside of the range!")
        print("Please try again!")
        guess = int(input("Guess a number between 1 and 20:"))
        numGuesses += 1
        count = count + 1
    elif guess > 20:
        print("You have guessed outside of the range!")
        guess = int(input("Guess a number between 1 and 20:"))
        numGuesses += 1
        count = count + 1
    elif guess < randNum:
        print("Your guess was too low! Try again!")
        guess = int(input("Guess a number between 1 and 20:"))
        numGuesses += 1
        count = count + 1
    elif guess > randNum:
        print("Your guess was too high! Try again!")
        guess = int(input("Guess a number between 1 and 20: "))
        numGuesses += 1
        count = count + 1
else:
    count==10
    print("My number was " + str(randNum))
    print("Play again!")

# When you guess the correct number
if guess == randNum:
    print("You guessed correctly!")
    print("You were able to guess the number in " + str(numGuesses) +  " guesses")
