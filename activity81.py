import random
playing = True
number = random.randint(0, 9)
print ("I'm thinking of a number between 0 and 9")
while playing:
    guess = int(input("What is your guess? "))
    if guess < number:
        print ("Too low")
    elif guess > number:
        print ("Too high")
    else:
        print ("You got it!")
        playing = False
        
        