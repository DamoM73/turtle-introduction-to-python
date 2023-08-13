###############################################
## write a program that askes the user for a ##
## number and then counts up to that number. ##
###############################################

number = int(input("Give number to count up to: "))

for count in range(number):
    print(count + 1)