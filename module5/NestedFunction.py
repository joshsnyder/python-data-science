# This program will accept a number as input and execute a function defined within another, aka nested function
# Joshua Snyder 02/16/2020

def main():
    print(doubler(input('Enter a whole number: ')))

def doubler(number):
    def doubleIt(number):
        numberInt = int(number)
        return numberInt * 2
    return doubleIt(number)

# Execute main program
main()
