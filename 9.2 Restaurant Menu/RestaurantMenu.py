# -*- coding: utf-8 -*-

print "*" * 40
print "Welcome to your personal Menu-Maker-System"
print "*" * 40

menu_dict = {}

while True:
    menuentry = raw_input("Which menu do you want to add? ")
    priceentry = raw_input("How much should %s cost? " % menuentry)

    menu_dict[menuentry] = priceentry
    print "Your menu is '" + menuentry + "' and it will cost " + priceentry + " Dollar"

    another = raw_input("Do you want to add another menu? (yes or no) ")

    if another.lower() == "no":
        break

print "*" * 40
print "Your complete menulist is: "
for item in menu_dict:
    print "%s, %s Dollar" % (item, menu_dict[item])

with open("menu.txt", "w+") as menu_file:
    for dish in menu_dict:
        menu_file.write("%s, %s Dollar" % (dish, menu_dict[dish]) + "; ")

print "*" * 40
print "Your complete menu was printed in file 'menu.txt'. Youre welcome!"