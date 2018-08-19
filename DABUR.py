# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from sklearn.matrics import accuracy_score
from io import StringIO
from sklearn import tree
import os
import matplotlib.pyplot as plt

data=pd.read_csv("C:\\Users\\s\\Desktop\\DABUR.NS.csv")
data
MA = data.Close.rolling(window=20).mean()
SD = data.Close.rolling(window=20).std()
data['UpperBB'] = MA + (2 * SD) 
data['LowerBB'] = MA - (2 * SD)

lowerBBValues=[]
for i in range(19,742):
    lowerBandValue=data['LowerBB'][i]
    lowerBBValues.append(lowerBandValue)
    
upperBBValues=[]
for i in range(19,742):
    upperBandValue=data['UpperBB'][i]
    upperBBValues.append(upperBandValue)
    
dates=[]
for i in range(20,742):
    date=data['Date'][i]
    dates.append(date)

pd.concat([MA,data.UpperBB,data.LowerBB,data.Close],axis=1).plot()

data2=data

sellDateLists=[]
buyDateLists=[]

#Code to store all the closing values in a seperate list
closingValueLists=[]
for i in range(20,742):
    temporaryCloseValue=data['Close'][i]
    closingValueLists.append(temporaryCloseValue)

#Code to store the dates when the Client should have bought the stock
for index in range(0,722):
    if(closingValueLists[index]<lowerBBValues[index] and index!=723):
        dateOfBuy=dates[index]
        buyDateLists.append(dateOfBuy)
        
#Code to store the dates when the Client should have sold the stock
for index in range(0,722):
    if(closingValueLists[index]>upperBBValues[index] and index!=723):
        dateOfBuy=dates[index]
        sellDateLists.append(dateOfBuy)


combineLists=[]
totalInvestment=1000000
noOfShares=0
buyPrice=0
sellPrice=0
buyFlag=1
sellFlag=1
oneTimeFlag="ON"
loop=1
noStepRequired=0

for index in range(0,722):
    if(closingValueLists[index]<lowerBBValues[index] and closingValueLists[index]<upperBBValues[index] and index!=723):
        combineLists.append(1)
    else:
        if(closingValueLists[index]>lowerBBValues[index] and closingValueLists[index]>upperBBValues[index] and index!=723):
            combineLists.append(-1)
        else:
            combineLists.append(0)
        
        
for i in range(0,722):
    indexValue=combineLists[i]
    if(indexValue==1 and buyFlag==1):
        buyPrice=closingValueLists[i]
        noOfShares=totalInvestment/buyPrice
        totalInvestment=0
        buyFlag=0
        sellFlag=1
    elif(indexValue==-1 and sellFlag==1):
        sellPrice=closingValueLists[i]
        totalInvestment=noOfShares*sellPrice
        noOfShares=0
        sellFlag=0
        buyFlag=1
    else:
        noStepRequired=noStepRequired+1

print("Total Profit or Loss made by an investor is....",totalInvestment)
print("Profit or Loss made by the company is....",totalInvestment-1000000)
print(noOfShares)
print(noStepRequired)
        
    
    
    
    
    