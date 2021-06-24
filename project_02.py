import random
randnum = random.randint(1,100)
yourguess = None
guesses = 0

while (yourguess != randnum):

    yourguess = int(input("Please enter your guess :"))
    guesses += 1

    if randnum == yourguess:
        print("Congratulation you guessed it right and you win")

    elif randnum > yourguess:
        print("You guees it wrong! please increase your number")

    elif randnum < yourguess:
        print("You guees it wrong! please decrease your number")


print(f"You guessed the number in {guesses} guesses")

with open('highscore1.txt') as f:
    highscore = int(f.read())

if guesses < highscore:
    print("You have just broken the record of high score")
    with open('highscore1.txt','w') as f:
        f.write(str(guesses))