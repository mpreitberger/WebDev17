# -*- coding: utf-8 -*-

print "-" * 20
print "-" * 20
print "FizzBuzz"
print "-" * 20
print "-" * 20

x = raw_input("Please enter a number between 1 and 100:" )
print "=" * 30
print "FizzBuzz starting..."
print " "

try:
    x = int(x)

    for num in range(1, x+1):
        if num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        elif num % 3 == 0 and num % 5 == 0:
            print "FizzBuzz"
        else:
            print num

except ValueError:
    print "You have to enter a valid number."
