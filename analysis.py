# This is a program which analysis' Ronald Fisher's Iris data set
# Author: Sarah McNelis

import numpy as np 
import matplotlib as plt
import pandas as pd 


filename = pd.read_csv('iris.csv')
df = pd.DataFrame(filename)

'''
filename = 'iris.csv'
df = pf.read_csv(filename)
'''
#print(df)
#print(df.head()) #prints top 5 rows 
#print(df.tail(7)) #prints last 7 rows 

#print(df.info(), file=f) #<<https://towardsdatascience.com/data-analysis-in-python-getting-started-with-pandas-8cbcc1500c83>>

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

maxvalues = df.groupby(["Sepal Length"])[['Petal Length']].mean()
print(maxvalues)


'''
# SUMMARY TO TXT FILE
with open ('summary.txt', 'wt') as f:
    f.write('The Iris Dataset: Statistics Summary of all Species\n')
    print(df.describe(), file=f) #gives brief analysis #<<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>> <<https://www.datasciencemadesimple.com/descriptive-summary-statistics-python-pandas/>>
    f.write('\nStactistics Summary of Iris-Setosa Species:\n',)
    print(df[df['Species'] == 'setosa'].describe(), file=f)
    f.write('\nStactistics Summary of Iris-Versicolor Species:\n')
    print(df[df['Species'] == 'versicolor'].describe(), file=f)
    f.write('\nStactistics Summary of Iris-Virginica Species:\n')
    print(df[df['Species'] == 'virginica'].describe(), file=f)
    f.write('\nShape of Iris Dataset:\n',)
    print(df.shape, file=f) #prints shape of data set
    f.write('\nFirst 5 rows of the Iris Dataset:\n')
    print(df.head(5), file=f)
    f.write('\nLast 7 rows of the Iris Dataset:\n')
    print(df.tail(7), file=f)
    f.write('\nCount of different Species\n')
    print(species, file=f) 
    f.write('\nMiddle Species\n')
    print(df[df['Species'] == 'versicolor'].head(6), file=f)





x = minvalues
y = maxvalues


# 'Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'
df.plot.scatter(meanvalues, maxvalues)
plt.show()

# To generate a Scatterplot using pandas #

df.plot(kind="scatter" , x="Sepal Lenght" , y="Sepal Width")
plt.show()
'''