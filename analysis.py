# This is program which analysis' Fisher's Iris data set
# Author: Sarah McNelis

# PROGRESS ON PROJECT
# MAPPED A PLAN OF HOW PROG SHOULD MAYBE GO?
# NEXT STEP WRITING CODE!!! 

#download iris data set
#https://www.kaggle.com/saurabh00007/iriscsv

# import modeules, numpy, malplotlib, 
import numpy as np 
import matplotlib as plt 
import math 

##### 1
# open csv file here for reading
# pandas here? view extra lecture to check
filename = 'iris.csv'
with open(filename) as f: #default as reading mode
    f.read()

# to view column headings
# https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447
# fyi sepal is green part of flower/bud after steam before petals 
df.head()

####### 2 VARIABLES
# how many variables?
# var 1 = how many species? 3... would look good on scatter plot ### count()

# var 2 = average/mean of first 10? or las 10? or random 10? of first 10 petal lenghts ?
#               maybe vs sepal lenghts? and maybe same for widths??
#               is this possible sarah????
#               https://www.w3schools.com/python/module_statistics.asp
#               statistics.mean()	Calculates the mean (average) of the given data
average = float(sum(numbers)) / len(numbers)


# var 3 = sum of widhts/ lenghts?
#           math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.) 
#           https://www.w3schools.com/python/module_math.asp 

# var 4 = lowest value of a list min()
#               import math

# var 5 = highest value of a list max()

######### 3 
# OUTPUT SUMMERARY OF VAR 1-5 INTO ONE TXT FILE

#########4
# histo, scatter and text file summary for each variable. 
#var1-5 histo each 
## https://www.w3schools.com/python/matplotlib_histograms.asp
xpoints = np.array()
ypoints = np.array()

font1 = {'family':'times new roman','color':'tab:red','size':30, 'weight':'bold', 'style':'oblique'}
font2 = {'family': 'times new roman', 'color':'indianred', 'size':20, 'weight':'semibold'}
font3 = {'family': 'times new roman', 'color':'slategrey', 'size':20, 'weight':'semibold'}
# creating fonts here for title and axis labels
# playing with font styles, color, sixe and weight

plt.hist(xpoints, ypoints1)

plt.xlabel('', fontdict=font2) #use fontdict to call fonts above
plt.ylabel('', fontdict=font3)
plt.title('', fontdict=font1, loc='center') #loc points to where title will appear on plot
plt.legend(loc='best', fontsize='large') 
plt.show()
#plt.savefig('hist 1   .png')
# have commented this out. can only either show or save. can't do both at same time.




######### 5 
#var 1-5 scatter each
#  https://www.w3schools.com/python/matplotlib_scatter.asp
xpoints = np.array()
ypoints = np.array()

font1 = {'family':'times new roman','color':'tab:red','size':30, 'weight':'bold', 'style':'oblique'}
font2 = {'family': 'times new roman', 'color':'indianred', 'size':20, 'weight':'semibold'}
font3 = {'family': 'times new roman', 'color':'slategrey', 'size':20, 'weight':'semibold'}
# creating fonts here for title and axis labels
# playing with font styles, color, sixe and weight

plt.scatter(xpoints, ypoints1)

plt.xlabel('', fontdict=font2) #use fontdict to call fonts above
plt.ylabel('', fontdict=font3)
plt.title('', fontdict=font1, loc='center') #loc points to where title will appear on plot
plt.legend(loc='best', fontsize='large') 
plt.show()
#plt.savefig('scatter 1   .png')
# have commented this out. can only either show or save. can't do both at same time.