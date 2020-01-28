# Module 3 a simple function that accepts a persons name, and prints it to the console as a greeting.
# Joshua Snyder 01/27/2020

# Utilize global variables for people's names
PeopleList = ("Josh", "Joe", "Adam")
PeopleDict = [{"First":"Josh","Last":"Snyder"},{"First":"Joe","Last":"Smith"}]
NumberList = [(33,44),(44,55),(66,77)]

# Simple function taking an argument and printing various messages
def simple_name_function(inputName):
    print("*** Simple name function ***")
    print("Hello " + inputName + " it's nice to meet you.")
    print(inputName + " what is your favorite hobby?")
    print("It was a pleasure meeting you " + inputName + " I hope we speak soon!")
    # Horizontal line for making iterations easier to read.
    print("_______________________")

def full_name_function(inputName):
    first = inputName["First"]
    last = inputName["Last"]
    print("*** Full name function ***")
    print("Hello " + first + " " + last + " it's nice to meet you.")
    # Horizontal line for making iterations easier to read.
    print("_______________________")

def simple_number_function(inputInt):
    print("*** Simple number function ***")
    sum = inputInt[0] + inputInt[1]
    print("Total for " + str(inputInt[0]) + " plus " + str(inputInt[1]) + " equals: " + str(sum))
    # Horizontal line for making iterations easier to read.
    print("_______________________")

def modified_number_function(inputInt):
    print("*** Modified number function ***")
    sum = inputInt[0] + inputInt[1]
    return sum

# Call functions passing in different inputs
for person in PeopleList:
    simple_name_function(person)

for person in PeopleDict:
    full_name_function(person)

for numbers in NumberList:
    simple_number_function(numbers)

for numbers in NumberList:
    sum = modified_number_function(numbers)
    print("Total for " + str(numbers[0]) + " plus " + str(numbers[1]) + " equals: " + str(sum))
    # Horizontal line for making iterations easier to read.
    print("_______________________")