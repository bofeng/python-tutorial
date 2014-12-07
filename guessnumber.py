import random
number = random.randint(1, 20)

win = False
hint = "What number I am thinking?"
for i in range(3):
    guess = raw_input(hint)
    guess = int(guess)
    if guess < number:
        hint = "I am thinking a bigger one"
    elif guess > number:
        hint = "I am thinking a smaller one"
    else:
        win = True
        print "You Win !!!"
        break

if not win:
    print "You Lose !!! The answer is "
    print number
