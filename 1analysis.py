#30032019 Investigate the DataSet Clodagh Murphy
#Code adapted from Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#1. load hardcoded data into a pandas dataframe
#A dataframe is the primary pandas structure of arranging data
#Import modules
import numpy as np
import pandas as pd

print("1. Load hardcoded data into a dataframe")
#I hardcoded a sample of 10 lines as it was tedious and unnecessary to format all 150 lines
#df is the globally accepted abbreviation for DataFrame
#the lists are passed through the command
df =pd.DataFrame(

    [[5.1,3.5,1.4,0.2,'Iris-setosa'],
    [4.9,3.0,1.4,0.2,'Iris-setosa'],
    [4.7,3.2,1.3,0.2,'Iris-setosa'],
    [4.6,3.1,1.5,0.2,'Iris-setosa'],
    [5.0,3.6,1.4,0.2,'Iris-setosa'],
    [5.4,3.9,1.7,0.4,'Iris-setosa'],
    [4.6,3.4,1.4,0.3,'Iris-setosa'],
    [5.0,3.4,1.5,0.2,'Iris-setosa'],
    [4.4,2.9,1.4,0.2,'Iris-setosa'],
    [4.9,3.1,1.5,0.1,'Iris-setosa']],
    index = [0,1,2,3,4,5,6,7,8,9],
    columns =['sepal length in cm','sepal width in cm','petal length in cm','petal width in cm','species'])
#The dataframe will be printed, it's similar to an excel table
print (df)