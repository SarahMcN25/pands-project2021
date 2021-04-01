# This is a program which analysis' Ronald Fisher's Iris data set
# Author: Sarah McNelis

import numpy as np 
import matplotlib as plt
import pandas as pd 
import math 

filename = 'iris.data' # !!!!!!! thinks first row is columns.... need to fix this SARAH!!!!!! 
df = pd.read_table(filename) #open the file and read the table
#print(df)
#rint(df.head(5)) #prints first 5 rows from top
#print(df.tail(7))
#print(df.shape) #prints shape of data set
print(df.describe()) #gives brief analysis