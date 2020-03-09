# The purpose of this program is to demistrate multiple iterator functions.
# Joshua Snyder 03/08/2020

# External modules
from itertools import *

# Global data sets
iterToolsData = ["a","b","c"]

def main():
    # Type 1 itertools basic
    ItertoolsFunction()
    # Type 2 infinite loop
    ItertoolsinfiniteFunction()
    # Type 3 cycle
    ItertoolsCycleFunction()
    # Type 4 repeat
    ItertoolsRepeatFunction()

def ItertoolsFunction():
    print("-----------------------------------")
    print("------- Itertools Example ---------")
    print("-----------------------------------")
    for i in iterToolsData:
        print(i)

def ItertoolsinfiniteFunction():
    print("-----------------------------------")
    print("----- infinite Loop Example -------")
    print("-----------------------------------")
    for i in count(10, 10):
        if i == 40:
            break
        print(str(i))
    
def ItertoolsCycleFunction():
    print("-----------------------------------")
    print("------- Cycle Loop Example --------")
    print("-----------------------------------")
    idx = 0
    for i in cycle(iterToolsData):
        idx += 1
        if idx == 10:
            break
        print(i)

def ItertoolsRepeatFunction():
    print("-----------------------------------")
    print("------- Repeat Loop Example --------")
    print("-----------------------------------")
    for i in repeat(iterToolsData, 3):
        print(i)

# Execute program
main()