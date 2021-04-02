# This is a program which analysis' Ronald Fisher's Iris data set
# Author: Sarah McNelis

import numpy as np 
import matplotlib as plt
import pandas as pd 
import math 


filename = 'iris.csv' 
df = pd.read_csv(filename) #open and read csv file 

#print(df)
print(df.head()) #prints top 5 rows 
#print(df.tail(7)) #prints last 7 rows 
#print(df.shape) #prints shape of data set
#print(df.describe()) #gives brief analysis #<<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>>
#print(df.info()) #<<https://towardsdatascience.com/data-analysis-in-python-getting-started-with-pandas-8cbcc1500c83>>


# var 1 = how many species - do scatter plot for this
species = df['Species'].value_counts()  #gives count of each species
print(species)                          # <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html>>




'''
# to get mean of column
meanvalues = df.columns('Sepal Lenght').mean()
print(meanvalues)

sumvalues = df.groupby('sepellenght').sum()
print(sumvalues)

minvalues = df.groupby('sepellenght').min()
print(minvalues)

maxvalues = df.groupby('sepellenght').max()
print(maxvalues)

# maybe create a function for each - mean, sum, min etc and then call function for each column???
# might be neater and less code???? Think about it!
''' 