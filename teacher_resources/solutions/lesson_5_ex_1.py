# Amy's security guard program

######################################################
## Write a program that asks for a person's name    ##
## and then grants entry of that person is Amy      ##
## everyone else is told, politely, to go away      ##
######################################################

person = input("Hi. Please provide your name: ")

if person == "Amy":
    print("Welcome Amy, please come in")
else:
    print("Politley go away")
    