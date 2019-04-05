#05042019 Investigate the DataSet
#Data Visualisation with pands and matplotlib functions
#Adapted from
# Basic Analysis of the Iris Data set Using Python by Oluwasogo Oluwafemi Ogundowole
#https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
#Import pandas and matplotlib modules
import pandas
import matplotlib.pyplot as plt

#Rename the iris dataset to "dataset"
dataset = pandas.read_csv('irisdataset.txt')

#Create a boxplot to view all the columns at once on the same scale which is helpful
#to put the data in context

plt.title ('BoxPlot - data visualisation of the iris dataset')
dataset.boxplot()
#Command to display the plot
plt.show()
