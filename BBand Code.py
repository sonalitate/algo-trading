# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:55:28 2018

@author: gupta
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('E:\\Sem 3\\Financial ANalytics 2\\Module 3 - Algo Trading\\Algo Case Study\\')
Container = pd.read_csv("Container Corporation.csv")
Cummins = pd.read_csv("CUMMINS.csv")
Dabur = pd.read_csv("DABUR.csv")
Dlf = pd.read_csv("DLF.csv")
Emami = pd.read_csv("EMAMI.csv")
General_Insurance = pd.read_csv("General Insurance.csv")
Godrejcp = pd.read_csv("GODREJCP.csv")

def null(x):
    return(x.isnull().sum())

def cal(x):
    x['MA'] = x['Close'].rolling(window=20).mean()
    x['STD'] = x['Close'].rolling(window=20).std()
    x['Upper Band'] = x['MA'] + (x['STD'] * 2)
    x['Lower Band'] = x['MA'] - (x['STD'] * 2)

def bband(x):
    x[['Close', 'MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
    plt.title('Bollinger Band')
    plt.ylabel('Price')
    plt.show();





null(Container)
cal(Container)
bband(Container)

null(Cummins)
cal(Cummins)
bband(Cummins)

null(Dabur)
cal(Dabur)
bband(Dabur)

null(Dlf)
cal(Dlf)
bband(Dlf)

null(Emami)
cal(Emami)
bband(Emami)

null(General_Insurance)
cal(General_Insurance)
bband(General_Insurance)

null(Godrejcp)
cal(Godrejcp)
bband(Godrejcp)
