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

#A histogram is an accurate representation of the distribution of numerical data
#This is a type of univariate analysis, i.e. looking at just one subset of the data at a time.
#A histogram relates only one variable

dataset.hist()
plt.show()
