# to test small sections of my analysis code
# not for final submittion
import pandas as pf

species = ()

##### 1
# open csv file here for reading
# pandas here? view extra lecture to check
iris = 'iris.data'

columns = []


#columns = ['sepallength','sepalwidth','petallength','petalwidth','typeofspecies']

with open(iris, encoding="utf-8") as f: #default as reading mode
    data = f.read()
    df.info() #<<https://towardsdatascience.com/data-analysis-in-python-getting-started-with-pandas-8cbcc1500c83>>
   # columns.append(data)
    
#print(columns)

'''
print("columns",iris.columns)
print("*********")
print("shape:",iris.shape)
print("*********")
print("Size:",iris.size)
print("*********")
print("no of samples available for each type") print(iris["type"].value_counts())
print("*********")
print(iris.describe())
'''