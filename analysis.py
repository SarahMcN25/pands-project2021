# This is a program which analysis' Ronald Fisher's Iris data set
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 

# <<https://realpython.com/pandas-groupby/>>
# Use 1 decimal places in output display
pd.set_option("display.precision", 1)
# Don't wrap repr(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)

#downloaded csv iris data set
#https://www.kaggle.com/saurabh00007/iriscsv
#downloaded .data @
#http://archive.ics.uci.edu/ml/datasets/Iris 
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

filename = pd.read_csv('iris.csv')
df = pd.DataFrame(filename)

#filename = 'iris.csv'
#df = pd.read_csv(filename)

#print(df)
#print(df.info(), file=f) 
#<<https://towardsdatascience.com/data-analysis-in-python-getting-started-with-pandas-8cbcc1500c83>>

species = df['Species'].value_counts()  #gives count of each species
#print(species)  
# <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html>>

# var 2 - Mean of all columns 
# <<https://www.statology.org/mean-of-column-pandas/>>
# <<https://www.w3schools.com/python/module_math.asp>>
meanvalues = df.mean()
#print(meanvalues)

# var 3 - sum of each column ### need to figure out how to omit the species column for these
#sum of widhts/ lenghts?
sumvalues = df.sum() 
#print(sumvalues)

# var 4 - lowest value for each column
minvalues = df.min()
#print(minvalues)

# var 5 - highest value for each column
#maxvalues = df.max()
#print(maxvalues)

# mean of each column of each species
meansetosa = df[df['Species'] == 'setosa'].mean()
meanversicolor = df[df['Species'] == 'versicolor'].mean()
meanvirginica = df[df['Species'] == 'virginica'].mean()
#print(maxsetosa'\n', maxversicolor'n', maxvirginica)
#print(maxsetosa)

# SUMMARY TO TXT FILE 
# <<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>> 
# <<https://www.datasciencemadesimple.com/descriptive-summary-statistics-python-pandas/>>
with open ('summary.txt', 'wt') as f:
    f.write('The Iris Dataset: Statistics Summary of all Species\n')
    print(df.describe(), file=f)                                    #gives brief analysis of all 
    f.write('\nCount of Different Species:\n')
    print(species, file=f)                                          # counts number of species
    f.write('\nShape of Iris Dataset:\n',)
    print(df.shape, file=f)                                         # prints shape of data set
    f.write('\nStatistical Summary of Iris Setosa Species:\n',)
    print(df[df['Species'] == 'setosa'].describe(), file=f)         # prints summary of setosa
    f.write('\nStatistical Summary of Iris Versicolor Species:\n')
    print(df[df['Species'] == 'versicolor'].describe(), file=f)     # prints summary of versicolor      
    f.write('\nStatistical Summary of Iris Virginica Species:\n')
    print(df[df['Species'] == 'virginica'].describe(), file=f)      # prints summary of virginica
    f.write('\nFirst 5 rows of the Iris Dataset:\n')
    print(df.head(5), file=f)                                       # pinrts top 5 rows
    f.write('\nLast 7 rows of the Iris Dataset:\n')
    print(df.tail(7), file=f)                                       # prints last 7 rows
    f.write('\nLast 4 Rows of Iris Setosa Species:\n')
    print(df[df['Species'] == 'setosa'].tail(4), file=f)            # prints last 4 rows of setosa
    f.write('\nFirst 6 Rows of Iris Versicolor Species:\n')
    print(df[df['Species'] == 'versicolor'].head(), file=f)         # prints top 6 rows of versicolor
    f.write('\nFirst 3 Rows of the Iris Virginica Species:\n')
    print(df[df['Species'] == 'virginica'].head(3), file=f)         # prints top 3 rows of virginica
    

#<<https://realpython.com/pandas-groupby/>>

# VAR 1 - count()
petalwidthcount = df.groupby(['Species'])[['Petal Width']].count()
#print(petalwidthcount)
sepalwidthcount = df.groupby(['Species'])[['Sepal Width']].count()
#print(sepalwidthcount)
petallenghtcount =df.groupby(['Species'])[['Petal Length']].count()
#print(petallenghtcount)
sepallenghtcount =df.groupby(['Species'])[['Sepal Length']].count()
#print(sepallenghtcount)

# VAR 2 - mean()
sepalwidthmean = df.groupby(['Species'])[['Sepal Width']].mean()
#print(sepalwidthmean)
sepallenghtmean =df.groupby(['Species'])[['Sepal Length']].mean()
#print(sepallenghtmean)
petalwidthmean = df.groupby(['Species'])[['Petal Width']].mean()
#print(petalwidthmean)
petallengthmean =df.groupby(['Species'])[['Petal Length']].mean()
#print(petallengthmean)

# VAR 3 - std()
petalwidthstd = df.groupby(['Species'])[['Petal Width']].std()
#print(petalwidthstd)
sepalwidthstd = df.groupby(['Species'])[['Sepal Width']].std()
#print(sepalwidthstd)
petallenghtstd =df.groupby(['Species'])[['Petal Length']].std()
#print(petallenghtstd)
sepallenghtstd =df.groupby(['Species'])[['Sepal Length']].std()
#print(sepallenghtstd)

# VAR 4 - min()
petalwidthmin = df.groupby(['Species'])[['Petal Width']].min()
#print(petalwidthmin)
sepalwidthmin = df.groupby(['Species'])[['Sepal Width']].min()
#print(sepalwidthmin)
petallenghtmin =df.groupby(['Species'])[['Petal Length']].min()
#print(petallenghtmin)
sepallenghtmin =df.groupby(['Species'])[['Sepal Length']].min()
#print(sepallenghtmin)

# VAR 5 - max()
petalwidthmax = df.groupby(['Species'])[['Petal Width']].max()
#print(petalwidthmax)
sepalwidthmax = df.groupby(['Species'])[['Sepal Width']].max()
#print(sepalwidthmax)
petallenghtmax =df.groupby(['Species'])[['Petal Length']].max()
#print(petallenghtmax)
sepallenghtmax =df.groupby(['Species'])[['Sepal Length']].max()
#print(sepallenghtmax)
'''
# NEED TO WORK ON THIS NEXT!!!
x = sepal width # need to make into list/array
y = count 
df.plot(kind='scatter', x, y)
plt.show()
'''
# HISTO 1: COUTNS
#SEPAL WIDTH VS PETAL WIDTH OF 3 SPECIES 
x1 = sepalwidthcount
x2 = petalwidthcount

plt.figure()
df.plot.scatter(x='Sepal Length', y='Sepal Width')
plt.show()

