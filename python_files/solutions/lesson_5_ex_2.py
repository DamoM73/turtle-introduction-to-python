# Amy's security guard program

friends = "Bruce"

######################################################
## Write a program that asks for a person's name    ##
## and then grants entry of that person is Amy      ##
## or a friend of Amy.                              ##
## Everyone else is told, politely, to go away      ##
######################################################

person = input("Hi. Please provide your name: ")

if person == "Amy":
    print("Welcome Amy, please come in")
elif person == friends:
    print("Welcom fiend of Amy's, please come in")   
else:
    print("Politley go away")