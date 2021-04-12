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

filename = pd.read_csv('iris.csv')
df = pd.DataFrame(filename)

#print(df)
#print(df.info(), file=f) 
#<<https://towardsdatascience.com/data-analysis-in-python-getting-started-with-pandas-8cbcc1500c83>>

species = df['Species'].value_counts()  #gives count of each species
#print(species)  #debug
# <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html>>

columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']


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
    
    # MAYBE PUT A CORRELATION IN HERE??

# <<https://seaborn.pydata.org/generated/seaborn.lmplot.html>>
# <<https://seaborn.pydata.org/examples/index.html>>
# 
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

# <<https://seaborn.pydata.org/generated/seaborn.histplot.html>>

# HISTOS
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

