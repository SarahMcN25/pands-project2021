# This is a program which analysis' Ronald Fisher's Iris data set
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 


# Adjust settings for output display - 1 decimal place
pd.set_option("display.precision", 1)


# open data set 
filename = pd.read_csv('iris.csv')
df = pd.DataFrame(filename)
#print(df) #debug


# SUMMARY TO TXT FILE 
with open ('summary.txt', 'wt') as f:
    f.write('The Iris Dataset: Statistics Summary of all Species\n')
    print(df.describe(), file=f)                                    # gives brief analysis of all 
    f.write('\nCount of Different Species:\n')
    print(df['Species'].value_counts(), file=f)                     # counts number of species
    f.write('\nShape of Iris Dataset:\n')
    print(df.shape, file=f)                                         # prints shape of data set
    f.write('\nStatistical Summary of Iris Setosa:\n',)
    print(df[df['Species'] == 'setosa'].describe(), file=f)         # prints summary of setosa
    f.write('\nStatistical Summary of Iris Versicolor:\n')
    print(df[df['Species'] == 'versicolor'].describe(), file=f)     # prints summary of versicolor      
    f.write('\nStatistical Summary of Iris Virginica:\n')
    print(df[df['Species'] == 'virginica'].describe(), file=f)      # prints summary of virginica
    f.write('\nFirst 5 rows of the Iris Dataset:\n')
    print(df.head(5), file=f)                                       # prints top 5 rows
    f.write('\nLast 7 rows of the Iris Dataset:\n')
    print(df.tail(7), file=f)                                       # prints last 7 rows
    f.write('\nLast 4 Rows of Iris Setosa Species:\n')
    print(df[df['Species'] == 'setosa'].tail(4), file=f)            # prints last 4 rows of setosa
    f.write('\nFirst 6 Rows of Iris Versicolor Species:\n')
    print(df[df['Species'] == 'versicolor'].head(), file=f)         # prints top 6 rows of versicolor
    f.write('\nFirst 3 Rows of the Iris Virginica Species:\n')
    print(df[df['Species'] == 'virginica'].head(3), file=f)         # prints top 3 rows of virginica

'''
# HISTOGRAMS

# Petal Length
def histPetalLength():
    plt.figure()
    sns.histplot(data=df, x='Petal Length', hue='Species', multiple='stack')
    plt.title('Petal Length in cm', size=14)
    plt.xlabel('Petal Length', size=11)
    plt.ylabel('Frequency', size=11)
    plt.savefig('histogramPetalLength.png')
    #plt.show()

# Petal Width
def histPetalWidth():
    plt.figure()
    sns.histplot(data=df, x='Petal Width', hue='Species', multiple='stack')
    plt.title('Petal Width in cm', size=14)
    plt.xlabel('Petal Width', size=11)
    plt.ylabel('Frequency', size=11)
    plt.savefig('histogramPetalWidth.png')
    #plt.show() 

# Sepal Length
def histSepalLength():
    plt.figure()
    sns.histplot(data=df, x='Sepal Length', hue='Species', multiple='stack')
    plt.title('Sepal Length in cm', size=14)
    plt.xlabel('Sepal Length', size=11)
    plt.ylabel('Frequency', size=11)
    plt.savefig('histogramSepalLength.png')
    #plt.show() 

# Sepal Width
def histSepalWidth():
    plt.figure()
    sns.histplot(data=df, x='Sepal Width', hue='Species', multiple='stack')
    plt.title('Sepal Width in cm', size=14)
    plt.xlabel('Sepal Width', size=11)
    plt.ylabel('Frequency', size=11)
    plt.savefig('histogramSepalWidth.png')  
    #plt.show()

# Calling the histogram functions here
histPetalLength()
histPetalWidth()
histSepalLength()
histSepalWidth()
'''

# SCATTERS
# <<https://matplotlib.org/stable/api/markers_api.html>> gives different symbols on scatter

# Petal Length vs Petal Width
def scatPLvPW():
    plt.figure()
    sns.scatterplot(x='Petal Length', y='Petal Width', data=df, hue='Species')
    plt.title('Petal Width vs Petal Length', size=16)
    plt.xlabel('Petal Length', size=12)
    plt.ylabel('Petal Width', size=12)
    plt.legend(loc='best')
    plt.savefig('scatterPetalLength_PetalWidth.png')
    #plt.show() 
    
# Sepal Length vs Sepal Width
def scatSLvSW():
    plt.figure()
    sns.scatterplot(x='Sepal Length', y='Sepal Width', data=df, hue='Species')
    plt.title('Sepal Width vs Sepal Length', size=16)
    plt.xlabel('Sepal Length', size=12)
    plt.ylabel('Sepal Width', size=12)
    plt.legend(loc='best')
    #plt.savefig('scatterSepalLength_SepalWidth.png')
    plt.show() 

# Petal Length vs Sepal Length
def scatPLvSL():
    plt.figure()
    sns.scatterplot(x='Petal Length', y='Sepal Length', data=df, hue='Species')
    plt.title('Petal Length vs Sepal Length', size=16)
    plt.xlabel('Petal Length', size=12)
    plt.ylabel('Sepal Length', size=12)
    plt.legend(loc='best')
    #plt.savefig('scatterPetalLength_SepalLength.png')
    plt.show() 

# Sepal Width vs Petal Width
def scatSWvPW():
    plt.figure()
    sns.scatterplot(x='Sepal Width', y='Petal Width', data=df, hue='Species')
    plt.title('Sepal Width vs Petal Width', size=16)
    plt.xlabel('Sepal Width', size=12)
    plt.ylabel('Petal Width', size=12)
    plt.legend(loc='best')
    #plt.savefig('scatterSepalWidth_PetalWidth.png')
    plt.show() 

# Petal Length vs Sepal Width
def scatPLvSW():
    plt.figure()
    sns.scatterplot(x='Petal Length', y='Sepal Width', data=df, hue='Species')
    plt.title('Petal Length vs Sepal Width', size=16)
    plt.xlabel('Petal Length', size=12)
    plt.ylabel('Sepal Width', size=12)
    plt.legend(loc='best')
    #plt.savefig('scatterPetalLength_SepalWidth.png')
    plt.show() 

# Sepal Length vs Petal Width
def scatSLvPW():
    plt.figure()
    sns.scatterplot(x='Sepal Length', y='Petal Width', data=df, hue='Species')
    plt.title('Sepal Length vs Petal Width', size=16)
    plt.xlabel('Sepal Length', size=12)
    plt.ylabel('Petal Width', size=12)
    plt.legend(loc='best')
    #plt.savefig('scatterSepalLength_PetalWidth.png')
    plt.show() 




