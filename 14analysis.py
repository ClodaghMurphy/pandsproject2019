#03042019 Investigate the DataSet
#Experimenting with pands functions
#Adapted from
# Basic Analysis of the Iris Data set Using Python by Oluwasogo Oluwafemi Ogundowole
#https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
#Import pandas module
import pandas
#I investigated the data with pandas commands set out in the above article
#Most of them have been covered previously in python programs in this repository 1analysis-13analysis



dataset = pandas.read_csv('irisdataset.txt')
print("14.0 Experimenting with five pands functions to show descriptive statistics")
print("'head' displays first 5 rows of the dataset")
print(dataset.head())
print("'tail' displays first 5 rows of the dataset")
print(dataset.tail())
print ("'describe' displays a statistical summary")
print(dataset.describe())
print ("'sample(5)' displays 5 rows at random")
print(dataset.sample(5)) 
print("'isnull().sum() returns null information contained in the dataset")
print(dataset.isnull().sum())

