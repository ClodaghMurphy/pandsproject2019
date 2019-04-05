#05042019 Investigate the DataSet
#Data Visualisation with pands and matplotlib functions
#Adapted from
# Basic Analysis of the Iris Data set Using Python by Oluwasogo Oluwafemi Ogundowole
#https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
#Import pandas and matplotlib modules
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

#Rename the iris dataset to "dataset"
dataset = pandas.read_csv('irisdataset.txt')

#A scattermatrix

scatter_matrix(dataset)
plt.show()
