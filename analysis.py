# This is a program which analysis' Ronald Fisher's Iris data set
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 

# Use 1 decimal places in output display
pd.set_option("display.precision", 1)

filename = pd.read_csv('iris.csv')
df = pd.DataFrame(filename)
#print(df)

df.info()
#print(df.info())

#count of each species
species = df['Species'].value_counts()  
#print(species)  #debug

# SUMMARY TO TXT FILE 
with open ('summary.txt', 'wt') as f:
    f.write('The Iris Dataset: Statistics Summary of all Species\n')
    print(df.describe(), file=f)                                    #gives brief analysis of all 
    f.write('\nCount of Different Species:\n')
    print(species, file=f)                                          # counts number of species
    f.write('\nShape of Iris Dataset:\n',)
    print(df.shape, file=f)                                         # prints shape of data set
    f.write('\nStatistical Summary of Iris Setosa:\n',)
    print(df[df['Species'] == 'setosa'].describe(), file=f)         # prints summary of setosa
    f.write('\nStatistical Summary of Iris Versicolor:\n')
    print(df[df['Species'] == 'versicolor'].describe(), file=f)     # prints summary of versicolor      
    f.write('\nStatistical Summary of Iris Virginica:\n')
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

# HISTOGRAMS
# PL
fig = plt.figure() # this keeps x and y within each plot
sns.histplot(x="Petal Length", data=df, hue='Species')
#plt.legend(loc='best')
#plt.show() 
plt.savefig('histogramPetalLength.png')

# SL
fig = plt.figure()
sns.histplot(x="Sepal Length", data=df, hue='Species')
#plt.legend(loc='best')
#plt.show() 
plt.savefig('histogramSepalLength.png')

# PW
fig = plt.figure()
sns.histplot(x="Petal Width", data=df, hue='Species')
#plt.legend(loc='best')
#plt.show() 
plt.savefig('histogramPetalWidth.png')

# SW
fig = plt.figure()
sns.histplot(x="Sepal Width", data=df, hue='Species')
#plt.legend(loc='best')
#plt.show() 
plt.savefig('histogramSepalWidth.png')    


# SCATTERS
# PL VS PW
fig = plt.figure() # this keeps x and y within each plot
sns.scatterplot(x="Petal Length", y="Petal Width", data=df, hue='Species')
plt.legend(loc='best')
#plt.show() 
plt.savefig('scatterPetalLength_PetalWidth.png')

# SL VS SW
fig = plt.figure()
sns.scatterplot(x="Sepal Length", y="Sepal Width", data=df, hue='Species')
plt.legend(loc='best')
#plt.show() 
plt.savefig('scatterSepalLength_SepalWidth.png')

# PL VS SL
fig = plt.figure()
sns.scatterplot(x="Petal Length", y="Sepal Length", data=df, hue='Species')
plt.legend(loc='best')
#plt.show() 
plt.savefig('scatterPetalLength_SepalLength.png')

# SW VS PW
fig = plt.figure()
sns.scatterplot(x="Sepal Width", y="Petal Width", data=df, hue='Species')
plt.legend(loc='best')
#plt.show() 
plt.savefig('scatterSepalWidth_PetalWidth.png')

# PL VS SW
fig = plt.figure()
sns.scatterplot(x="Petal Length", y="Sepal Width", data=df, hue='Species')
plt.legend(loc='best')
#plt.show() 
plt.savefig('scatterPetalLength_SepalWidth.png')

# SL VS PW
fig = plt.figure()
sns.scatterplot(x="Sepal Length", y="Petal Width", data=df, hue='Species')
plt.legend(loc='best')
#plt.show() 
plt.savefig('scatterSepalLength_PetalWidth.png')




