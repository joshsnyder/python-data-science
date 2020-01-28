# Module 3 a simple function that accepts a persons name, and prints it to the console as a greeting.
# Joshua Snyder 01/27/2020

# Utilize global list for peoples names
People = ("Josh", "Joe", "Adam")

# Simple function taking an argument and printing various messages
def simple_name_function(inputName):
    print("Hello " + inputName + " it's nice to meet you.")
    print(inputName + " what is your favorite hobby?")
    print("It was a pleasure meeting you " + inputName + " I hope we speak soon!")
    # Horizontal line for making iterations easier to read.
    print("_______________________")

# Call the function passing in different inputs
for person in People:
    simple_name_function(person)