import csv
import datetime
import numpy as np

def openEncoding(fileName):
    with open(fileName, 'r') as f:
        reader = csv.reader(f, delimiter = ',')
        encoding = list(reader)
        encoding = np.array(encoding[0])

    encoding = encoding.astype(np.float)
    print(type(encoding[0]))
    print(encoding[0])
    

openEncoding('Obama.csv')
