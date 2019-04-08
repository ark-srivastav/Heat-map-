#reading csv files

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logging.info('Module Name: second.py \n Module Purpose : to calculate Yearly Average')

path='../Monthly Rain/'    # directory where data in form of CSV file is Stored
filename='Lakshadweep .csv' #As an example :)



# function which takes file name as input and returns calculated yearly average
def yearlyAverage(filename): 
    f=pd.read_csv(path+filename)  # adds filepath to file name and gets appropriate directory and reads the required .csv file
    years=f.loc[:,('Year')].unique()   # extract the unique months and years in separate arrays
    months=f.loc[:,('Month')].unique()
    #print("No of years",len(years))
    #print("No of Months",len(months))

    sum=[]
    monSum=0.0
    for y in years:            # Calculating Yearly Average Rainfall <the data is saved in form of Data per month per year>
        for m in months:
            temp=f.loc[(f['Year']==y)&(f['Month']==m),'Value']
            for j in temp:
                if j!='N.A.':
                    monSum=monSum+float(j)                                     
            monSum=monSum/12.0
            sum.append(monSum)
            monSum=0.0

    # No of Monthly Averages
    #print(len(sum))
    yrSum=0.0
    for x in sum:
        yrSum=yrSum+x
    #print("Yearly Average ",yrSum/len(years))
    return yrSum/len(years)

#Actual Output for Lakshwadeep.csv
#< INFO:root:Module to calculate Yearly Average
#  No of years 7
#  No of Months 12
#  84
#  Yearly Average  148.01666666666668
# >  


#yearlyAverage(filename)   # go ahead and uncomment this along with other print() functions to get a deeper look




