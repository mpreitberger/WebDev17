# -*- coding: utf-8 -*-

print "-" * 20
print "-" * 20
print "FizzBuzz"
print "-" * 20
print "-" * 20

x = raw_input("Please enter a number between 1 and 100:" )
print x

try:
    x = int(x)

    for num in range(x, 100):
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
