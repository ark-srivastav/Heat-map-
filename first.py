import glob
import numpy as np
import pandas as pd
import second #user defined Module
import logging
import csv 
logging.basicConfig(level=logging.INFO)
logging.info("Module Name : first.py \n Module Purpose : Getting the List of Files of .csv format of every State of India")

path='*.csv'
x=[]   #For storing the file names
files=glob.glob(path)
#print(len(files))
y=0.0
for c in files:
    y=second.yearlyAverage(c)
    #print(c[:-5]," ",y)
    x.append([c[:-4].upper(),y])

#print(x)
# with open('stateAndValue','w') as csvFile:
#     writer=csv.writer(csvFile)
#     writer.writerows(x)
# csvFile.close()
#accessing file names in directory