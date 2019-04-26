## pandsproject2019

## 1. Introduction
This repository contains pandsproject2019.<br>  
Using Fisher's Iris data set, I will explain the basic principles of investigating a data set <br>
and how Python can be used in the endeavour.<br>
## 2. A summary of the data set - what is it? why is it important?
  
According to wikipedia, https://en.wikipedia.org/wiki/Iris_(plant):
    
    >'Iris is a genus of 260–300 species of
    > flowering plants with "showy" flowers.'
    
    
The flower takes its name from the Greek word for a rainbow and is also the name for the Greek goddess of the rainbow, Iris.<br>
Three Iris varieties are used in the Iris flower data set outlined by Ronald Fisher in his 1936 paper "The <br>
use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis. <br> 
Discriminant analysis means that the aim is to classify the flower species from the four measurements provided in the dataset.<br>

CONTENTS OF THE IRIS DATASET<br>
The Data Set consists of information about 50 flowers from Iris setosa, Iris virginica and Iris versicolor
(three species of Iris).
Measurements of 
1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm <br>
were recorded along with the species.<br>

Therefore, the dataset consists of 150 rows and 4 columns.

This is a sample line from the Irish data set in csv format:<br>
*5.1,3.5,1.4,0.2,Iris-setosa*<br>
This data indicates a sepal length of 5.1cm, sepal width of 3.5cm, petal length of 1.4cm and petal width of 0.2cm<br>
Petals are the colourful part of a flower that surround the reproductive elements, the sepals (usually green but not in this instance!) protect the bud and support the petals after budding.<br>
These measurements belong to an Iris-setosa flower collected as part of the experiment in 1936.<br>

 The Iris Data Set is important because<br>
   (a) it is considered to be one of the most versatile datasets available in pattern recognition literature, <br>
   (b) it is an ideal sample to use when learning about data analysis due to it's compact nature (150 lines) and high accuracy, <br>
   (c) Ronald Fisher's original 1936 paper proves that once measurements are available it is possible predict the variety of Iris with a high degree of accuracy- an important tenet of data analysis.<br>

## 3. My investigations into the Iris Data Set - Process and Observations 

i. I made a plan in relation how the project would proceed. The project description had (usefully) set out what is required for a minimum viable project, I would use this as a template.  The most challenging part for me was how to run Python code to investigate the data set. I really didn't know what that would entail or how to apply the scripting I had learned so far, other than plotting a function with matplotlib.  I found youtube tutorials very useful in getting to grips with the new python libraries.  Lots of the online articles mentioned pandas and matplotlib but also sci-kit learn.  I decided to focus on the former two tools and then, if time allowed, dip a little into machine learning.


ii. I read online articles/watched youtube videos on the subject of the dataset and wrote a summary, see section 2 above.  


iii. I started a list of references in the README to populate over the course of the project.  


iv. I downloaded the Data Set (1999 version) and Data Set Description from  http://archive.ics.uci.edu/ml/datasets/Iris I downloaded and saved images of the three types of iris which I thought might help me understand the data set better. It didn't - they are still very difficult to distinguish visually!  
![alt text](https://github.com/ClodaghMurphy/pandsproject2019/blob/master/iris%20x3%20images.png)


<br>v.   During lectures, I had been introduced to numpy, pandas and matplotlib.
I read more about pandas - the open source python library that provides high level data analysis tools.   
It runs on top of numPy - a foundational data structure for many python libraries including matplotlib (see further information below).<br> 


vi. I used python code to familiarise myself with pandas and how it can be used to investigate the iris dataset.  
I used [Joe James youtube tutorial](https://www.youtube.com/watch?v=e60ItwlZTKM) as a key source of information.  He includes a print command at the start of every script which helpfully outputs a description of what that script does, I used this convention in addition to comments where possible on all my scripts in this project.  Most of the code was copied verbatim from other coders who have been referenced.  In order to ensure I can provide evidence that I am developing new knowledge and skills I used #comments to document that I understand what the code does - it's not simply cut and pasted from another site!  In this regard there was very little troubleshooting involved, however it is documented when there was.  Sometimes I think that experienced coders leave little errors in their scripts to challenge the "noobs"...and that is fair enough.  :beginner:<br>


vii.I learned that pandas is an efficient tool that displays/arranges the data in a meaningful way usually with just one command. 
The "dataframe" is the primary pandas structure of arranging data - something like a table in excel. The scripts detailed in the table below returned information such as information about the index, count, mean, standard deviation, minimum, maximum, 25/50/75 percentiles. 
Pandas commands can also be used to change the titles of variables and assign new fields.


viii.The df.dtypes command returned the numerical data as being "float64" data type, this is how  
pandas refers to floating point numbers.  The species of flower was classified as an object.  

Item in dataset | Data Type
------------ | -------------
sepal length in cm | float64
species  | object


ix. Matplotlib is a python library that can create 2D graphs and plots.  I have used it to create a box plot.  Box plots get the name from the box in the middle of the diagram and are a way to display numerical data via their quartiles. In the figure that is rendered:  
- the minimum is represented by the lowermost line (a "whisker")  
- the maximum value is the uppermost line (a "whisker")  
- the lowermost end of each box is quartile 1, the uppermost represents quartile 3  
- the second quartile (the median) is the line inside the box.  
- the circles that appear on the plot for "sepal width in cm" indicate data that is outside the median, unusual recordings compared to the majority of the data  
- a compact box indicates less variation in the values, as shown in the box plot directly below relating to iris sepals while the petal length can vary from approx 1,5 cm to 5 cm.
I have written scripts that display univariate (single variable) and multivariate (two or more variables) versions of boxplots<br>
![alt text](https://github.com/ClodaghMurphy/pandsproject2019/blob/master/Univariate%20Boxplot.png)
<br>x. Histograms represent one variable in a visualisation (different from a bar chart which relates two!).  
The height indicates how many flowers are in a particular range.
Using matplotlib, it is a very simple command to create a histogram and this is the philosophy behind the library - "make easy things easy and hard things possible".  <br>
![alt text](https://github.com/ClodaghMurphy/pandsproject2019/blob/master/Histogram.png)

xi I used matplotlib to plot a scattermatrix displays all the fields on both x and y axis, so it's a lot of information in one image.  
The variables are represented in both scatterplots and histograms.  
A scattermatrix provides an overview that shows connections between the data and is used to identify structured relationships between types of data.


xii. The analysis I have detailed so far is considered to be exploring the data using "descriptive statistics", it's a starting point to help understand 
the data by summarising what you have (as opposed to making predictions or inferential statistics).<br>Important statistics to set out are what is normal (central) and what is at the outermost ranges (variability, spread, deviation).  
A box plot can provide a lot of these statistics in one image i.e., the boxes are what is central while the outlier circles represent the deviations.  

![alt text](https://github.com/ClodaghMurphy/pandsproject2019/blob/master/Multivariate%20Boxplot.png "Multivariate Box Plot")

xiii. [Ben Hamner](https://www.kaggle.com/benhamner/sepal-width-vs-length) is a founding member of the kaggle website and published an article in 2016 on the Iris Dataset.  In his graph all 50 setosa flowers can be seen lying distinctly separate, the other 100 flowers merge.  Therefore, he proves with a scatter graph that the setosa species is "linearly separable" from the other two in the data set.    
  
ivx. The standard deviation is a measurement statisticians use for the amount of variability (or spread)   
among the numbers in a data set. As the term implies, a standard deviation is a standard (or typical) amount of   
deviation (or distance) from the average (or mean, as it is usually referred to by statisticians).  


xv. Having first analysed the data set, I attempt to draw some conclusions by plotting scatterplots and interpreting them.  
Comparison of "like with like" (i.e. petals with petals) should provide more meaningful results. I used scatterplots to compare petals and then sepals. The plot produced in 21analysis.py illustrates that in terms of petals, setosa species are the smallest, virginica the largest and versicolor roughly in the middle.  For sepals - the widest ones belong to the setosa species, the narrowest to versicolor with virginica in the middle although there is some cross-over between the last two species.  
![alt text](https://github.com/ClodaghMurphy/pandsproject2019/blob/master/Scatterplot.png "Scatterplot Plot")

xvi A brief look at machine learning and scikit-Learn. <br>Machine learning is the technique of using computers to extract knowledge and gain insight into data.  Supervised learning in machine learning attempts to build structures that apply to new data and predict answers, therefore a human may not know what the correct answer is.  I consider the iris dataset to be a great starting point because an absolute beginner can start to see patterns in the data simply by using scatterplots and boxplots (point xv. above), thereby helping to understand the ideas and how machine learning might work when the machine can see patterns a human cannot.  I found the concept to be a very steep learning curve from the analysis done up to now.  The topic will be explored in greater detail in future modules of this course and I'm looking forward to developing a greater understanding.

- Scikit-Learn is a python library that is used for machine learning and statistical modelling.  
I learned about some of the terminology used in relation to scikit-learn and machine learning e.g. features and targets.
The iris dataset is so popular that it is built into scikit-learn.  I found commands to print data, feature names, target and target names. 
- k-NN refers to the nearest neighbour algorithm, where observations of data are used to predict a response by learning the relationship
between the features and targets. The value of k parameter is input by the user, 1 means you want the closest prediction while k=15 indicates results from 1-15 "nearest neighbours" are required.
To choose 1 may give an inaccurate answer depending on the array, whereas a result of 15 predictions may need further analysis, it all depends on the user's requirements. It's a straighforward algorithm and a good one to use for a small dataset.
- Analysis23 code copied more or less verbatim from [Msanjayds on github](https://github.com/Msanjayds/Scikit-learn/blob/master/KNN%20on%20Iris%20Datset.ipynb) with explanatory comments by me, illustrates how to predict with the KNN algorithm, then plot the relationship between K and testing accuracy scores. Metrics, train_test_split modules are used so it is a super example to provide a taster of what machine learning can involve.




## 4. How to run the python code used to investigate the data set        
On github.com choose the "Clone or download" button to copy the code onto your machine.<br>
For further information on how github works video guides are available here https://www.youtube.com/githubguides<br>
The latest version of Python can be downloaded from https://www.python.org/downloads/<br>
If you don't have a preferred CLI, the IDLE graphical user interface will be automatically installed when you download from this site and can be used for running python programs.<br>


## 5. What the Python Code does


Python Code File Name | Description
------------ | -------------
1Analysis  | Loads a segment of hardcoded data into a dataframe
2Analysis | Reads a text file into a dataframe
3Analysis | Top and tail the list
4Analysis  | Print the data types in the data set
5Analysis  | Print index details
6Analysis  | Print column titles
7Analysis  | Print values contained in the table/dataframe
8Analysis  | Print statistical summary of the data
9Analysis | Sort the records by a particular column or columns
10Analysis | Print slices of data
11Analysis | Assignment of values into cells and new columns
12Analysis | Rename columns 
13Analysis | Write the dataframe to a csv or xls file 
14Analysis | 5 pandas commands to display descriptive statistics 
15Analysis | Generate univariate boxplot 
16Analysis | Generate histogram
17Analysis | Generate scatter matrix 
18Analysis | Generate multivariate boxplot
19Analysis | Print standard deviation for each column
20Analysis | Generate 2 scatter plots to compare sepals and petals
21Analysis | Generate 2 scatter plots to compare sepals and petals with species identified 
22Analysis | Print a list of data pertaining to each species in descending order 
23Analysis | Print data using scikit-learn library
24Analysis | Predict with the KNN algorithm, then plot the relationship


## 6. References used in completing the project
        
https://en.wikipedia.org/wiki/Iris_(plant) <br>
https://en.wikipedia.org/wiki/Linear_discriminant_analysis<br>
https://www.analyticsvidhya.com/blog/2018/05/
24-ultimate-data-science-projects-to-boost-your-knowledge-and-skills/<br>

Data School youtube videos:
Getting started in scikit-learn with the famous iris dataset<br>
https://www.youtube.com/watch?v=hd1W4CyPX58<br>
Training a machine learning model with scikit-learn<br>
https://www.youtube.com/watch?v=RlQuVL6-qe8<br>
https://towardsdatascience.com/the-5-basic-statistics-concepts-data-scientists-need-to-know-2c96740377ae<br>
http://archive.ics.uci.edu/ml/datasets/Iris<br>
http://www.twofrog.com/irissetosa.html<br>
https://gardengoodsdirect.com/product/iris-versicolor/<br>
https://www.fs.fed.us/wildflowers/beauty/iris/Blue_Flag/iris_virginica.shtml<br>
Joe James "Python: Pandas Tutorial | Intro to DataFrames"
https://www.youtube.com/watch?v=e60ItwlZTKM<br>
Basic Analysis of the Iris Data set Using Python
by Oluwasogo Oluwafemi Ogundowole<br>
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342<br>
Definition - What does Scalar mean?<br>
https://www.techopedia.com/definition/16441/scalar<br>
Univariate Analysis: Definition, Examples<br>
https://www.statisticshowto.datasciencecentral.com/univariate/<br>
Box Plot<br>
https://en.wikipedia.org/wiki/Box_plot<br>
Understanding & Comparing Boxplots (Box and Whisker Plots)<br>
https://www.youtube.com/watch?v=Hm6Mra5XJSs<br>
Histogram<br>
https://en.wikipedia.org/wiki/Histogram<br>
Interpreting Histograms<br>
https://www.youtube.com/watch?time_continue=50&v=ImU4ftpihf8<br>
What is a Scatter Plot?<br>
https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/regression-analysis/scatter-plot-chart/#definition<br>
Understanding Descriptive Statistics <br>
https://towardsdatascience.com/understanding-descriptive-statistics-c9c2b0641291 <br>
Standard deviation<br>
https://wiki.kidzsearch.com/wiki/Standard_deviation<br>
Calculating the mean and std on excel file using python<br>
https://stackoverflow.com/questions/33034243/calculating-the-mean-and-std-on-excel-file-using-python<br>
Statistical Analysis of the Iris Flower Dataset <br>
http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf<br>
Python - IRIS Data visualization and explanation<br>
https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation<br>
Iris Species: Classify iris plants into three species in this classic dataset<br>
https://www.kaggle.com/benhamner/sepal-width-vs-length<br>
Supervised learning: predicting an output variable from high-dimensional observations<br>
https://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html<br>
KNN (using scikit-learn) on Iris dataset <br>
https://github.com/Msanjayds/Scikit-learn/blob/master/KNN%20on%20Iris%20Datset.ipynb<br>
How to split your dataset to train and test datasets using SciKit Learn<br>
https://medium.com/@contactsunny/how-to-split-your-dataset-to-train-and-test-datasets-using-scikit-learn-e7cf6eb5e0d<br>
why plt.show() shows one extra blank figure<br>
https://stackoverflow.com/questions/43237079/why-plt-show-shows-one-extra-blank-figure<br>
matplotlib.pyplot.subplots<br>
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html<br>
