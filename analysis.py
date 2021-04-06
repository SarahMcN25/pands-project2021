# This is a program which analysis' Ronald Fisher's Iris data set
# Author: Sarah McNelis

import numpy as np 
import matplotlib as plt
import pandas as pd 

#downloaded csv iris data set
#https://www.kaggle.com/saurabh00007/iriscsv
#downloaded .data @
#http://archive.ics.uci.edu/ml/datasets/Iris 
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

filename = pd.read_csv('iris.csv')
df = pd.DataFrame(filename)

'''
filename = 'iris.csv'
df = pf.read_csv(filename)
'''
#print(df)
#print(df.head()) #prints top 5 rows 
#print(df.tail(7)) #prints last 7 rows 

#print(df.info(), file=f) 
#<<https://towardsdatascience.com/data-analysis-in-python-getting-started-with-pandas-8cbcc1500c83>>

# var 1 = how many species - do scatter plot for this
species = df['Species'].value_counts()  #gives count of each species
#print(species)                          # <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html>>

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

# max of each column of each species
maxsetosa = df[df['Species'] == 'setosa'].max()
maxversicolor = df[df['Species'] == 'versicolor'].max()
maxvirginica = df[df['Species'] == 'virginica'].max()
#print(maxsetosa, maxversicolor, maxvirginica)
# (df[df['Species'] == 'setosa'].describe(), file=f)
# [df['Species'] == 'versicolor'].describe(), file=f)
# (df[df['Species'] == 'virginica'].describe(), file=f)
# 'Sepal Length'
# 'Sepal Width'
# 'Petal Lenght'
# 'Petal Width'
# 'Species'

#<<https://realpython.com/pandas-groupby/>>
petalwidthmean = df.groupby(['Species'])[['Petal Width']].mean()
print(petalwidthmean)

petallenghtmean =df.groupby(['Species'])[['Petal Length']].mean()
print(petallenghtmean)

sepalwidthmean = df.groupby(['Species'])[['Sepal Width']].mean()
print(sepalwidthmean)

sepallenghtmean =df.groupby(['Species'])[['Sepal Length']].mean()
print(sepallenghtmean)


# SUMMARY TO TXT FILE
with open ('summary.txt', 'wt') as f:
    f.write('The Iris Dataset: Statistics Summary of all Species\n')
    print(df.describe(), file=f) #gives brief analysis #<<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>> <<https://www.datasciencemadesimple.com/descriptive-summary-statistics-python-pandas/>>
    f.write('\nCount of Different Species:\n')
    print(species, file=f) 
    f.write('\nShape of Iris Dataset:\n',)
    print(df.shape, file=f) #prints shape of data set
    f.write('\nStatistical Summary of Iris Setosa Species:\n',)
    print(df[df['Species'] == 'setosa'].describe(), file=f)
    f.write('\nStatistical Summary of Iris Versicolor Species:\n')
    print(df[df['Species'] == 'versicolor'].describe(), file=f)
    f.write('\nStatistical Summary of Iris Virginica Species:\n')
    print(df[df['Species'] == 'virginica'].describe(), file=f)
    f.write('\nFirst 5 rows of the Iris Dataset:\n')
    print(df.head(5), file=f)
    f.write('\nLast 7 rows of the Iris Dataset:\n')
    print(df.tail(7), file=f)
    f.write('\nFirst 6 Rows of Iris Versicolor Species:\n')
    print(df[df['Species'] == 'versicolor'].head(), file=f)
    f.write('\nLast 4 Rows of Iris Setosa Species:\n')
    print(df[df['Species'] == 'setosa'].tail(4), file=f)
    f.write('\nFirst 3 Rows of the Iris Virginica Species:\n')
    print(df[df['Species'] == 'virginica'].head(3), file=f)


'''


x = minvalues
y = maxvalues


# 'Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'
df.plot.scatter(meanvalues, maxvalues)
plt.show()

# To generate a Scatterplot using pandas #

df.plot(kind="scatter" , x="Sepal Lenght" , y="Sepal Width")
plt.show()
'''