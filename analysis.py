# This is a program which analysis' Ronald Fisher's Iris data set
# Author: Sarah McNelis

import numpy as np 
import matplotlib as plt
import pandas as pd 
import math 

filename = 'iris.data'
with open(filename, encoding="utf-8") as f: #default as reading mode
    data = f.read()
    df = pd.DataFrame(data)
    print(df)
    print(df.describe())