# -*- coding: utf-8 -*-

import random

def main():
    secret = random.randint(1, 5)

    while True:
        guess = int(raw_input("Guess a number between 1 and 5: "))
        if guess == secret:
            print "Congrats! You did good!"
        else:
            print "Thats wrong, try again"

if __name__ == "__main__":
    main()