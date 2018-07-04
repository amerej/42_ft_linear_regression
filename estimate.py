from __future__ import division
import csv
import sys
import math
import matplotlib.pyplot as plt

def input_km():
    mileage = 0
    while True:
       print('Please enter a mileage: ')
       try:
           choice = input()
       except EOFError:
           error('EOF on input. Exit..')
           sys.exit(0)
       except:
           error('Unknown error on input. Exit...')
           sys.exit(0)
       if type(choice) == int:
           mileage = int(choice)
           break
           error('{}: Not a valid value'.format(choice))
    return mileage

def main():
    filename = "results.csv"
    teta0 = []
    teta1 = []
    estimate = 0
    mileage = 0

    with open(filename, "rb") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            teta0.append( row[0] )
            teta1.append( row[1] )
        
    mileage = input_km()
    estimate = float(teta0[0]) + (float(teta1[0]) * mileage / 10000)

    print(estimate)

if __name__ == "__main__":
    main()
