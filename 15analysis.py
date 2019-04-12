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

#Create a boxplot for each of the four columns.
#This is a type of univariate analysis, i.e. looking at just one subset of the data at a time.

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)

#Command to display the plot

plt.show()
