# This program will accept standard input from console, utilize datetime library and various modules of datetime.
# And conditionally print the output based on number of tabs between the input from console.
# Joshua Snyder 03/01/2020

import sys
from datetime import datetime
from datetime import time
from datetime import date

def main():
    date = datetime.now()
    time = date.strftime("%X")
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 4:
            store, item, cost, payment = data
            print (f"{str(date)}\t{str(time)}\t{store}\t{item}\t{cost}\t{payment}")
        

# Execute
main()