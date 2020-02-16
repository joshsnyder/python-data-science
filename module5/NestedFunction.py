# This program will accept a number as input and execute a function defined within another, aka nested function
# Joshua Snyder 02/16/2020

def doubler(number):
    def doubleIt(number):
        return (number * 2)
    return doubleIt

doubler2 = doubler(2)
doubler4 = doubler(4)

print(doubler2(2))
print(doubler4(4))

