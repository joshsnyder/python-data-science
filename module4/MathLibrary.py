# Module 4 a simple program to compute roots and factorials of input
# Joshua Snyder 02/08/2020

import math
def main():
    print("------------------------------------------")
    print('Welcome to the basics of the Math library')
    print("------------------------------------------")
    print()
    print()
    inputValue = 'enter'
    while not str(inputValue).__contains__('exit')  :
        inputValue = eval(input('Please enter a whole number: '))
        print()
        print('Input.......: ' + str(inputValue))
        print()
        if not str(inputValue).__contains__('exit') :
            print('Sqrt........: ' + str(math.sqrt(inputValue)))
            print('Factorial...: ' + str(math.factorial(inputValue)))
            print()
    print("------------------------------------------")
    print('Thanks for stopping by :) ')
    print("------------------------------------------")
# Call program
main()
    
