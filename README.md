## **PANDS-PROJECT 2021**
### Author: Sarah McNelis - G00398343
&nbsp;
### **Introduction** 
The aim of this project is to research, investigate and analyse Fisher's Iris data set. I have written a program in python to complete this task. I have also included a full list of references and resources used. First let's take a look at the man behind the data set.
&nbsp;
### **Ronald Fisher**
Sir Ronald Fisher (17 February 1890 – 29 July 1962) was a British statistician, eugenicist, and biologist. One of his most popular developments was the Iris flower data set also known as Fisher's Iris data set. It is a multivariate data set introduced by Ronald Fisher in his 1936 paper on _The use of multiple measurements in taxonomic problems_ as an example of linear discriminant analysis(LDA). The purpose of LDA as explained by Wikipedia is to portray the difference between classes of data.
# ![fisher](imageFisher.jpg) 
### **Iris Flower Data Set**
The dataset contains a set of 150 records under five attributes - Sepal Length, Sepal Width, Petal Length, Petal Width and Species. 
# ![flowers](imageFlowers.jpg)
These records are broken down into three species: Iris-Setosa, Iris-Versicolor and Iris-Virginica. Each species contains 50 records each. Therefore, it is not a surprise that this data set became a popular test case for many statistical classification techniques in machine learning such as support vector machines (SVMs). Wikipedia explains that SVMs are supervised learning models with associated learning algorithms that examine data for classification and analysis.
### **The Research**
- The first step of this project was reseaching the Iris data set. I downloaded the data set in a csv file format from Kaggle. I then decided to explore the different attributes of the data set. I found some images online which clarify which part of Iris flower is the sepal and which part is the petal. Sepals are usually green and offers support and protection to the petal. However, the sepal of the Iris flower is typically a shade of purple. The role of the petal is to surround and protect the reproductive part of the flower.
# ![sepalPetal](imageSepalPetal.jpg)
- The second step of this project was developing the code. This required importing various modules required to complete the analysis. Numpy and matplotlib are used for plotting the analysis, seaborn is a good tool for visualisation when plotting and pandas is used for analysing the data frame. After this I decided to do a bit of housekeeping. Pydata descibes numerous settings that can be changed using pandas. I set the program to only allow one decimal place in the output display; pd.set_option('display.precision', 1). The number refers to the amount of floating points you wish to allow. I have chosen one decimal place as it is neater and easier to read.
- Next I opened the csv file in write mode in order to begin the analysis. w3schools explains the different modes that can be used when opening a file. The 'w' stands for write mode and the 't' referes to text mode as opposed to 'b' for binary. At this point I have also given a name to the file in which I am writing the analysis to; summary.txt. After this, I began investigating the different ways I could analysise this data set. My first discovery was the function describe(). Pydata explains the parameters and purpose of this function. As you can see from the image below, using describe() gives a statical summary of the data frame in tabular form. These summaries include the count, mean, standard deviation, minimun value, percentiles and maximun values of each attribute. 
# ![describe()](imageDescribeAll.jpg)
- I then used the count() function which pydata explains will return a series containing counts of unique values. In this program this function has given a count of each of the different species within the data frame.We can also see from this image that the shape of this data frame is reported as (150, 5). This means that the Iris data set consists of 150 rows and 5 columns. Pydata explains that the shape() function will return a tuple containing the dimensionality of the data frame.
# ![count/shape](imageCount_Shape.jpg)
- Subsequently, I decided to break down the statical analysis for each of the three species using the describe() function again. These tables give a brief summary of each species which are also broken down into four columns showing the sepal length, sepal width, petal length and petal width.
# ![describe()](imageDescribeEach.jpg)
- I then decided to select the first five rows form the top of the data frame using the head() function and also the last seven rows from the bottom using the tail() function as suggested by pydata. Afterward, I discovered that I could not only select the head and tail of the whole data frame but also the three species specifically like I did with the describle function. As you can see in the below image there are numerous ways of breaking down and analysing this data frame. 
# ![headAndTail](imageHead_Tail.jpg)
- The next step involved plotting this analysis. For this I have chosen to use a def statement when writing the different plots. I decided to do this as it is easier to organise my code and the functions can be easily accessed and used again (VanderPlas 2016, p. 41-42). The two most important factors to remember when using functions are that the local variables contained within the function cannot be called outside of that function and that a function does nothing unless it is called (Sweigart 2015, p. 61-67). Therefore, after creating functions for these plots I have then called them in order for them to run. 
- First, I created a histogram for each of the attributes; sepal length, sepal width, petal length, petal width. I have saved these histograms as png files in this respository. Within each of these histograms I choose to break down the results showing each attribute of each species as you can see in the below image. Sharma (2021) explains how to use hue for layered categorisation of histograms in the seaborn module. I have done this by passing in the attribute Species when creating the histograms; hue='Species'. This alows us to analysise each attribute of each species. Sharma (2021) also explains that using the feature 'stack' can allow for better visualization of each category. This is why I also added the parameter; multiple='stack', when creating the histograms. As we can see from this image these features are invaluable in allowing us to analysis the data of each attribute in this data frame. 
# ![histograms](image_Histograms.jpg)
- Next step was to create a scatterplot for each pair of variables. For this part of the task I decided to compare the following attributes:
    1. Petal Lenght and Petal Width 
    2. Sepal Lenght and Sepal Width
    3. Petal Lenght and Sepal Lenght
    4. Sepal Width and Petal Width
    5. Petal Lenght and Sepal Width 
    6. Sepal Lenght and Petal Width  

For each of these plots I have assigned an attribute to the x and y axis'. I have also used the hue feature again for the scatterplots. This will breakdown of the species when comparing each pair of variables. Similarily to the histograms I have used seaborn when creating the scatterplots as it allows for better visualisation. This makes it easier to compare each pair of variables.  
# ![scatterplots](image_Scatters.jpg)
- Finally, the last step of this program was developing another function to create a pairplot for this dataset. Pydata explains that searborn pairplot composes a grid of axes sharing each numeric variable in the data set across the y-axis in a single row and the x-axis across a single column. Again, I have chosen to use the feature hue in order to plot the different species in different colors. This pairplot will automatically form scatterplots and I have also chosen to use a histogram for the diagonal subplots by adding the element; diag_kind='hist'. This can be clearly seen in the below image.  
# ![pairplot](imagePairplot.jpg)
### **Conclusion** 
After completing the data analysis of Fisher's Iris data set I have determined that there is a wealth of information available on this particular data frame. I used a substantial amount of resources in my research and development of my python program. There are numourous ways that this data set can be analysed and manipulated. I have used various functions to analyise the data set including exploring the shape of the data frame, the count of species present and a brief stactical summary of the data frame and of each species. I have also used both hisograms and scatterplots to plot this analysis out. In my opinon, the most noticable aspect of my analysis is the distinct difference between the Iris-Setosa attributes in comparassion to the Iris-Versicolor and the Iris-Virginica. When you consider the pairplot in particular which gives a full overview of the data frame, the Iris-Versicolor and the Iris-Virginica seem to be similar in all aspects than the Iris-Setosa. Nonetheless, all three species are divisible from one another. And this may be another reason that Fisher's Iris data set is so popular amongst researchers in the data analyitics.  
## **References/Resources used:**
a

b

c

d
- _Descriptive or Summary Statistics in Python Pandas - Describe()_, (2021). Datasciencemadesimple. Available at: <<https://www.datasciencemadesimple.com/descriptive-summary-statistics-python-pandas/>> [Accessed April, 2021]

e

f

g



- <<https://www.geeksforgeeks.org/reading-csv-files-in-python/#:~:text=1%20USing%20csv.reader%20%28%29%3A%20At%20first%2C%20the%20CSV,a%20CSV%20file%20using%20pandas%20library%20functions.%20>>

h

i

j

k
- <<https://www.kaggle.com/arshid/iris-flower-dataset>>
- <<https://www.kaggle.com/saurabh00007/iriscsv>>

l

m
- _matplotlib.pyplot.scatter()_, (2020). Geeksforgeeks. Available at: <<https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/>> [Accessed April, 2021]


- <<https://machinelearningknowledge.ai/seaborn-histogram-plot-using-histplot-tutorial-for-beginners/>>
n

o

p
- _Plotting Histogrma in Python using Matplotlib_, (2020). Geeksforgeeks. Available at: <<https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/>> [Accessed April, 2021]


- <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html>>
- <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html>>
- <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html>>
- <<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>>
- <<https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html >> 
- <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.plotting.scatter_matrix.html>>
- <<https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html>>
- <<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html>>
- <<https://pythonspot.com/matplotlib-scatterplot/>>


q

r
- <<https://realpython.com/pandas-groupby/>>
- <<https://realpython.com/python-csv/#:~:text=Reading%20from%20a%20CSV%20file%20is%20done%20using,does%20the%20heavy%20lifting.%20Here%E2%80%99s%20the%20employee_birthday.txt%20file%3A>>
- <<https://realpython.com/python-histograms/>>

s
- <<https://seaborn.pydata.org/examples/index.html>>
- <<https://seaborn.pydata.org/generated/seaborn.histplot.html>>
- <<https://seaborn.pydata.org/generated/seaborn.lmplot.html>>
- <<https://www.statology.org/mean-of-column-pandas/>>
- Sweigart, A 2015, Automate The Boring Stuff with Python, William Pollock, San Francisco.

t
- <<https://towardsdatascience.com/data-analysis-in-python-getting-started-with-pandas-8cbcc1500c83>>

u

v
- VanderPlas, J 2016, A Whirlwind Tour of Python, O’Reilly Medica Inc, Sebastopol.
w
- <<https://en.wikipedia.org/wiki/Iris_flower_data_set>>
- <<https://en.wikipedia.org/wiki/Iris_(plant)>>
- <<https://en.wikipedia.org/wiki/Linear_discriminant_analysis>>
- <<https://en.wikipedia.org/wiki/Machine_learning>>
- <<https://en.wikipedia.org/wiki/Petal>>
- <<https://en.wikipedia.org/wiki/Ronald_Fisher>>
- <<https://en.wikipedia.org/wiki/Sepal>>
- <<https://en.wikipedia.org/wiki/Support-vector_machine>>
- <<https://www.w3schools.com/python/matplotlib_histograms.asp>>
- <<https://www.w3schools.com/python/matplotlib_scatter.asp>>
- <<https://www.w3schools.com/python/module_math.asp>>
- <<https://www.w3schools.com/python/python_file_handling.asp>>
- <<https://www.w3schools.com/python/python_functions.asp>>
x
 
<<https://seaborn.pydata.org/generated/seaborn.pairplot.html>>
y

z
