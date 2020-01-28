# Module 3 a simple function that accepts a persons name, and prints it to the console as a greeting.
# Joshua Snyder 01/27/2020

# Utilize global variables for below functions names
PeopleList = ("Josh", "Joe", "Adam")
PeopleDict = [{"First":"Josh","Last":"Snyder"},{"First":"Joe","Last":"Smith"},{"First":"Adam","Last":"Doe"}]
NumberList = [(33,44),(44,55),(66,77)]
x = [1, 2, 3, 4, 5]
y = [11, 12, 13, 14, 15]
z = [21, 22, 23, 24, 25]

# Simple function taking an argument and printing various messages
def simple_name_function(inputName):
    print("*** Simple name function ***")
    print("Hello " + inputName + " it's nice to meet you.")
    print(inputName + " what is your favorite hobby?")
    print("It was a pleasure meeting you " + inputName + " I hope we speak soon!")
    # Horizontal line for making iterations easier to read.
    print("________________________________________________________________________")

def full_name_function(inputName):
    first = inputName["First"]
    last = inputName["Last"]
    print("*** Full name function ***")
    print("Hello " + first + " " + last + " it's nice to meet you.")
    # Horizontal line for making iterations easier to read.
    print("________________________________________________________________________")

def simple_number_function(inputInt):
    print("*** Simple number function ***")
    sum = inputInt[0] + inputInt[1]
    print("Total for " + str(inputInt[0]) + " plus " + str(inputInt[1]) + " equals: " + str(sum))
    # Horizontal line for making iterations easier to read.
    print("________________________________________________________________________")

def modified_number_function(inputInt):
    print("*** Modified number function ***")
    sum = inputInt[0] + inputInt[1]
    return sum

def module_3_question_3(x, y, z):
    print("*** Module 3 question 3 ***")

    # 3 * x
    x3 = 0
    for num in x:
        x3 += (3 * num)

    # 3 * z
    z3 = 0
    for num in z:
        z3 += (3 * num)

    # x + y
    xySum = 0
    xySub = 0
    xSum = 0
    ySum = 0
    for num in x:
        xSum += num 
    for num in y:
        ySum += num
    xySum = (xSum + ySum)
    xySub = (xSum - ySum)

    # z + y
    zySum = 0
    zySub = 0
    zSum = 0
    ySum = 0
    for num in z:
        zSum += num 
    for num in y:
        ySum += num
    zySum = (zSum + ySum)
    zySub = (zSum - ySum)

    print("What is the value of 3*x? Answer: " + str(x3))
    print("What is the value of x+y? Answer: " + str(xySum))
    print("What is the value of x-y? Answer: " + str(xySub))
    print("What is the value of x[1]? Answer: " + str(x[1]))
    print("What is the value of x[0]? Answer: " + str(x[0]))
    print("What is the value of x[-1]? Answer: " + str(x[-1]))
    print("What is the value of x[:]? Answer: " + str(x[:]))
    print("What is the value of x[2:4]? Answer: " + str(x[2:4]))
    print("What is the value of x[1:4:2]? Answer: " + str(x[1:4:2]))
    print("What is the value of x[:2]? Answer: " + str(x[:2]))
    print("What is the value of x[::2]? Answer: " + str(x[::2]))
    print("What is the result of the following two expressions? x[3]=8 Answer: " + str(x[3]))
    print("________________________________________________________________________")
    print("What is the result of the above pair of expressions if the list x were replaced with the tuple z? Answers: ")
    print("________________________________________________________________________")
    print("What is the value of 3*z? Answer: " + str(z3))
    print("What is the value of z+y? Answer: " + str(zySum))
    print("What is the value of z-y? Answer: " + str(zySub))
    print("What is the value of z[1]? Answer: " + str(z[1]))
    print("What is the value of z[0]? Answer: " + str(z[0]))
    print("What is the value of z[-1]? Answer: " + str(z[-1]))
    print("What is the value of z[:]? Answer: " + str(z[:]))
    print("What is the value of z[2:4]? Answer: " + str(z[2:4]))
    print("What is the value of z[1:4:2]? Answer: " + str(z[1:4:2]))
    print("What is the value of z[:2]? Answer: " + str(z[:2]))
    print("What is the value of z[::2]? Answer: " + str(z[::2]))
    print("What is the result of the following two expressions? z[3]=8 Answer: " + str(z[3]))

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
    print("________________________________________________________________________")

module_3_question_3(x, y, z)