# A program to solve two equations; a quadratic one and a reciprocal one
# Joshua Snyder 02/08/2020

import math
def main():
    # Solve quadratic equation
    print('-----------------------------------------------------')
    print('Attempting to solve the following quadratic equation:')
    print('x^2 - 5.86x + 8.5408')
    print('-----------------------------------------------------')
    
    solution = quadraticFunc()
    print('The solution to problem 1 is: ' + str(solution))
    print()

    # Solve reciprocal equation
    print('------------------------------------------------------')
    print('Attempting to solve the following reciprocal equation:')
    print('Decimal representation of; 1/2 thru 1/10')
    print('------------------------------------------------------')

    reciprocalFunc()
    

def quadraticFunc():
    # Configure proper variables for equation
    a = 1
    b = -5.86
    c = 8.5408
    quadA = (2*a)
    powB = math.pow(b,2)
    quadC = (4*a*c)
    quadBMinusC = (powB - quadC)
    sqrtQuadBMinusC = math.sqrt(quadBMinusC)
    posAnswer = (-b + sqrtQuadBMinusC) / quadA
    negAnswer = (-b - sqrtQuadBMinusC) / quadA

    # Solve
    print(f'Coefficients: a = {a}, b = {b}, and c = {c}')
    print(f'Quadratic formula input: x = {-b} +- sqrt({b}^2 - 4*{a}*{c}) / 2*{a}')
    print(f'Quadratic formula cont: x = {-b} +- sqrt({powB} - {quadC}) / {quadA}')
    print(f'Quadratic formula cont: x = {-b} +- sqrt({quadBMinusC}) / {quadA}')
    print(f'Quadratic formula cont: x = {-b} +- {sqrtQuadBMinusC} / {quadA}')
    print()
    return (f'x = {posAnswer} or x = {negAnswer}')
    
def reciprocalFunc():
    # Configure decimals from 1/2 thru 1/10 fractions
    decimals = [('1/2',0.5),('1/3',1/3),('1/4',1/4),('1/5',1/5),('1/6',1/6),('1/7',1/7),('1/8',1/8),('1/9',1/9),('1/10',1/10)]
    print('The following fractions in decimal form are:')
    for dec in decimals:
        print(f'{dec}')

# Execute program
main()