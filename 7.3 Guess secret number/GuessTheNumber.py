# -*- coding: utf-8 -*-

secret = 5

guess = int(raw_input("Guess a number between 1 and 5: "))
print guess

if guess == 5:
    print "Congrats! You did good!"
elif guess == 1:
    print "Sorry, that's wrong."
elif guess == 2:
    print "Sorry, that's wrong."
elif guess == 3:
    print "Sorry, that's wrong."
elif guess == 4:
    print "Sorry, that's wrong."
else:
    print "You only can pick a number between 1 and 5. Please try again!"
