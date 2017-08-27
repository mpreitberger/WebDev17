# -*- coding: utf-8 -*-

print "Hello! With this program you can convert kilometers in miles."
print "You simple have to fill in, how many kilometers you want to convert."
print "-" * 10

while True:

    try:
        kilometers = raw_input("Enter Kilometers: ")
        kilometers = float(kilometers)
        miles = kilometers * 0.6214
        print kilometers, "kilometer are", miles, "miles."
    except ValueError:
        print "You have to use valid numbers!"
    again = raw_input("Do you want to convert another number of kilometers? ")
    if again.lower() in ("yes", "y"):
        print "Go ahead!"
    elif again.lower() in ("no", "n"):
        print "Shutdown"
        break
    else:
        print "You should have entered Yes, Y, No oder N. Please start program again."
        break