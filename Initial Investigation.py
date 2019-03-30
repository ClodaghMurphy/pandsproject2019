#30032019 Investigate the DataSet
#Import modules
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as 

#pandas will be used to load the dataset
#We will also use pandas next to investigate the data both with 
# (1) descriptive statistics 
# (2) data visualization.

dataset = pandas.read_csv('irisdataset.csv')


#Experimenting with pands functions
#dataset.head() check the first 10 rows of the data set
#dataset.tail() display last 10 row of the data set
#dataset.describe() gives a statistical summary 
#dataframe.sample(5) display 5 rows at random from the data set 
#dataframe.isnull().sum() a command to return the null info contained