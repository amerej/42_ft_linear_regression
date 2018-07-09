from __future__ import division
import csv
import sys
import math
import matplotlib.pyplot as plt
import os.path

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
    teta0 = [0.0]
    teta1 = [0.0]
    estimate = 0
    mileage = 0

    if (os.path.isfile(filename)):
        with open(filename, "rb") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            try:
                for row in reader:
                    teta0[0] = row[0]
                    teta1[0] = row[1]
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

    mileage = input_km()
    estimate = float(teta0[0]) + (float(teta1[0]) * mileage / 10000)

    print('Price: {}'.format(int(estimate)))

if __name__ == "__main__":
    main()
