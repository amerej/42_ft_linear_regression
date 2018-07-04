from __future__ import division
import csv
import math
import matplotlib.pyplot as plt

def main():
    filename = "data.csv"
    nb_iteration = 6000
    nb_elem = 0 
    learning_r = 0.01 
    km = []
    price = []

    with open(filename, "rb") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            km.append( row[0] )
            price.append( row[1] )
        km.pop(0)
        price.pop(0)
        
        nb_elem = len(km) 
        teta0 = 0
        teta1 = 0

        for iteration in xrange(0, nb_iteration):
            tmp0 = 0
            tmp1 = 0
    
            for i in xrange(0, nb_elem):
                 tmp0 += ( teta0 + ( teta1 * (int(km[i])/10000) ) - int(price[i]) )
                 tmp1 += ( teta0 + ( teta1 * (int(km[i])/10000) ) - int(price[i]) ) * (int(km[i]) / 10000)

            teta0 -= learning_r * (float(1) / nb_elem) * tmp0
            teta1 -= learning_r * (float(1) / nb_elem) * tmp1
        
        print(teta0, teta1)
        plt.plot(km, price, "ro")
        plt.show()

if __name__ == "__main__":
    main()
