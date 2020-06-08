# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:01:12 2020

@author: Gary Perrier
"""

import pandas as pd
#the data is included in the data folder included with this script
data = pd.read_csv('data/final_data.csv')
data.set_index('Date',inplace=True)
#create subset dataframes for each month so we can calculate monthly averages
#for max/min temp and precipitation
Jan = data.loc['1/1/2019':'1/31/2019']
Feb = data.loc['2/1/2019':'2/28/2019']
Mar = data.loc['3/1/2019':'3/31/2019']
Apr = data.loc['4/1/2019':'4/30/2019']
May = data.loc['5/1/2019':'5/31/2019']
Jun = data.loc['6/1/2019':'6/30/2019']
Jul = data.loc['7/1/2019':'7/31/2019']
Aug = data.loc['8/1/2019':'8/31/2019']
Sep = data.loc['9/1/2019':'9/30/2019']
Oct = data.loc['10/1/2019':'10/31/2019']
Nov = data.loc['11/1/2019':'11/30/2019']
Dec = data.loc['12/1/2019':'12/31/2019']
#calculating the averages for each month
JanMax = Jan['MaxTemperature'].mean()
JanMin = Jan['MinTemperature'].mean()
JanPre = Jan['Precipitation'].mean()

FebMax = Feb['MaxTemperature'].mean()
FebMin = Feb['MinTemperature'].mean()
FebPre = Feb['Precipitation'].mean()

MarMax = Mar['MaxTemperature'].mean()
MarMin = Mar['MinTemperature'].mean()
MarPre = Mar['Precipitation'].mean()

AprMax = Apr['MaxTemperature'].mean()
AprMin = Apr['MinTemperature'].mean()
AprPre = Apr['Precipitation'].mean()

MayMax = May['MaxTemperature'].mean()
MayMin = May['MinTemperature'].mean()
MayPre = May['Precipitation'].mean()

JunMax = Jun['MaxTemperature'].mean()
JunMin = Jun['MinTemperature'].mean()
JunPre = Jun['Precipitation'].mean()

JulMax = Jul['MaxTemperature'].mean()
JulMin = Jul['MinTemperature'].mean()
JulPre = Jul['Precipitation'].mean()

AugMax = Aug['MaxTemperature'].mean()
AugMin = Aug['MinTemperature'].mean()
AugPre = Aug['Precipitation'].mean()

SepMax = Sep['MaxTemperature'].mean()
SepMin = Sep['MinTemperature'].mean()
SepPre = Sep['Precipitation'].mean()

OctMax = Oct['MaxTemperature'].mean()
OctMin = Oct['MinTemperature'].mean()
OctPre = Oct['Precipitation'].mean()

NovMax = Nov['MaxTemperature'].mean()
NovMin = Nov['MinTemperature'].mean()
NovPre = Nov['Precipitation'].mean()

DecMax = Dec['MaxTemperature'].mean()
DecMin = Dec['MinTemperature'].mean()
DecPre = Dec['Precipitation'].mean()

#Creating a data frame for each so it is easy to graph
#I know how ugly this is but it would always throw back a sytax error when I
#tried to space it out on multiple lines
Max = {'month':['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November','December'], 'Temp':[JanMax, FebMax, MarMax, AprMax, MayMax, JunMax, JulMax, AugMax, SepMax, OctMax, NovMax, DecMax]}
Max = pd.DataFrame(Max)
Max.set_index('month',inplace=True)
Min = {'month':['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November','December'], 'Temp':[JanMin, FebMin, MarMin, AprMin, MayMin, JunMin, JulMin, AugMin, SepMin, OctMin, NovMin, DecMin]}
Min = pd.DataFrame(Min)
Min.set_index('month',inplace=True)
Pre = {'month':['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November','December'], 'Precip':[JanPre, FebPre, MarPre, AprPre, MayPre, JunPre, JulPre, AugPre, SepPre, OctPre, NovPre, DecPre]}
Pre = pd.DataFrame(Pre)
Pre.set_index('month',inplace=True)

#graphing the data
Max.plot(color='red', figsize=[10,5], title = '2019 Searcy, AR Average Max Temperature (F)')
Min.plot(color='blue', figsize=[10,5], title = '2019 Searcy, AR Average Min Temperature (F)')
Pre.plot(color='purple', figsize=[10,5] , title = '2019 Searcy, AR Average Precipitation (Inches)')
