#https://en.wikipedia.org/wiki/Iris_flower_data_set
#https://en.wikipedia.org/wiki/Ronald_Fisher

# PROGRESS ON PROJECT
# MAPPED A PLAN OF HOW PROG SHOULD GO
# NEXT STEP ADD MORE CODE
# START WITH READING IN CSV FILE - divide data into the 3 species
# THEN ANALYSISING DATA (VARIABLES HERE)
# WRITING TO TEXT FILE
# NEXT HISTOGRAM OF ALL VARIABLES
# FINALLY SCATTER PLOT OF VARIABLES 

#downloaded csv iris data set
#https://www.kaggle.com/saurabh00007/iriscsv

#downloaded .data @
#http://archive.ics.uci.edu/ml/datasets/Iris 
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/

# import modeules, numpy, malplotlib, 
import numpy as np 
import matplotlib as plt
import pandas as pd 
import math 

species = ()
x, y, z = species
##### 1
# open file here for reading
# pandas here? view extra lecture to check 
### maybe need to use pandas to read columns??

filename = 'iris.data'
with open(filename, encoding="utf-8") as f: #default as reading mode
    data = f.read().describe()
    getspecies = data['Species'].value_counts()
    species.append(getspecies) # append species to list. assign each species to x y z 

#print(x)
#print(y)
#print(z)
    
   


# Give description of dataset
# (f.describe()) <<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>>

## or open like below

iris = pd.read_csv('Iris.csv') # to view the data # 
iris.head()    

iris['Species'].value_counts()  # Generate a sample from each species #  



# to view column headings
# <<https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447>>
# fyi sepal is green part of flower/bud after steam before petals 

print(iris.head()) # Overview of Species Distribution from the  start #
print(iris.tail()) # Overview of Species Distribution from the end #
print(iris.shape) # prints shape of dataset

####### 2 VARIABLES
# how many variables?
# var 1 = how many species? 3... would look good on scatter plot ### count()

# var 2 = average/mean of first 10? or las 10? or random 10? of first 10 petal lenghts ?
#               maybe vs sepal lenghts? and maybe same for widths??
#               <<https://www.w3schools.com/python/module_statistics.asp>>
#               statistics.mean()	Calculates the mean (average) of the given data
def average():
    firstspecies = float(sum(x)) / len(x)
    secondspecies = float(sum(y)) / len(y)
    thirdspecies = float(sum(z)) / len(z)
    print(float(statistics.mean(firstspecies, secondspecies, thirdspecies))

# var 3 = sum of widhts/ lenghts?
#           math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.) 
#           <<https://www.w3schools.com/python/module_math.asp>>

# var 4 = lowest value of a list min()
#               import math 

# var 5 = highest value of a list max()

######### 3 
# OUTPUT SUMMERARY OF VAR 1-5 INTO ONE TXT FILE
with open("summary.txt", "wt") as f:
    f.write(str(summary, file=f)
    pd.set_option("display precision", 2) #to set everything to display 2 decimal places




#########4
# histo, scatter and text file summary for each variable. 
#var1-5 histo each 
## https://www.w3schools.com/python/matplotlib_histograms.asp
## https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/ 
## https://realpython.com/python-histograms/ 

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
# plt.show()
plt.savefig('hist 1   .png')
# have commented this out. can only either show or save. can't do both at same time.

DataFrame.hist() # plots the histograms of the columns on multiple subplots:
data.hist(by=np.random.randint(0, 4, 1000), figsize=(6, 4)) 
#The by keyword can be specified to plot grouped histograms:#
###### https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html 

######### 5 
#var 1-5 scatter each
#  https://www.w3schools.com/python/matplotlib_scatter.asp
## https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/
## https://pythonspot.com/matplotlib-scatterplot/ 
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
#plt.show()
plt.savefig('scatter 1   .png')
# have commented this out. can only either show or save. can't do both at same time.

# this plot all together??
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.plotting.scatter_matrix.html
# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html #scatter matrix see below
df = pd.DataFrame(np.random.randn(1000, 4), columns=["a", "b", "c", "d"])
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal="kde")


pd.plotting.scatter_matrix(f)
plt.show()
'''