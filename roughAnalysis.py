# Don't wrap repr(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)


##### dont think i need this.....

# mean of each column of each species
meansetosa = df[df['Species'] == 'setosa'].mean()
meanversicolor = df[df['Species'] == 'versicolor'].mean()
meanvirginica = df[df['Species'] == 'virginica'].mean()
#print(maxsetosa'\n', maxversicolor'n', maxvirginica)
#print(maxsetosa)

##### or this
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


#<<https://realpython.com/pandas-groupby/>>

# VAR 1 - count()
petalwidthcount = df.groupby(['Species'])[['Petal Width']].count()
#print(petalwidthcount) #debug
sepalwidthcount = df.groupby(['Species'])[['Sepal Width']].count()
#print(sepalwidthcount) #debug
petallenghtcount =df.groupby(['Species'])[['Petal Length']].count()
#print(petallenghtcount) #debug
sepallenghtcount =df.groupby(['Species'])[['Sepal Length']].count()
#print(sepallenghtcount) #debug

# VAR 2 - mean()
sepalwidthmean = df.groupby(['Species'])[['Sepal Width']].mean()
#print(sepalwidthmean) #debug
sepallenghtmean =df.groupby(['Species'])[['Sepal Length']].mean()
#print(sepallenghtmean) #debug
petalwidthmean = df.groupby(['Species'])[['Petal Width']].mean()
#print(petalwidthmean) #debug
petallengthmean =df.groupby(['Species'])[['Petal Length']].mean()
#print(petallengthmean) #debug

# VAR 3 - std()
petalwidthstd = df.groupby(['Species'])[['Petal Width']].std()
#print(petalwidthstd) #debug
sepalwidthstd = df.groupby(['Species'])[['Sepal Width']].std()
#print(sepalwidthstd) #debug
petallenghtstd =df.groupby(['Species'])[['Petal Length']].std()
#print(petallenghtstd) #debug
sepallenghtstd =df.groupby(['Species'])[['Sepal Length']].std()
#print(sepallenghtstd) #debug

# VAR 4 - min()
petalwidthmin = df.groupby(['Species'])[['Petal Width']].min()
#print(petalwidthmin) #debug
sepalwidthmin = df.groupby(['Species'])[['Sepal Width']].min()
#print(sepalwidthmin) #debug
petallenghtmin =df.groupby(['Species'])[['Petal Length']].min()
#print(petallenghtmin) #debug
sepallenghtmin =df.groupby(['Species'])[['Sepal Length']].min()
#print(sepallenghtmin) #debug

# VAR 5 - max()
petalwidthmax = df.groupby(['Species'])[['Petal Width']].max()
#print(petalwidthmax) #debug
sepalwidthmax = df.groupby(['Species'])[['Sepal Width']].max()
#print(sepalwidthmax) #debug
petallenghtmax =df.groupby(['Species'])[['Petal Length']].max()
#print(petallenghtmax) #debug
sepallenghtmax =df.groupby(['Species'])[['Sepal Length']].max()
#print(sepallenghtmax) #debug









# HISTOS

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
###### 

# SCATTERS 

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


 #scatter matrix see below
df = pd.DataFrame(np.random.randn(1000, 4), columns=["a", "b", "c", "d"])
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal="kde")

pd.plotting.scatter_matrix(f)
plt.show()
