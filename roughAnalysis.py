#https://en.wikipedia.org/wiki/Iris_flower_data_set
#https://en.wikipedia.org/wiki/Ronald_Fisher


# HISTOS
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

# SCATTERS
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
