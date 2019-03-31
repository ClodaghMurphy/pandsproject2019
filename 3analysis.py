#30032019 Investigate the DataSet Clodagh Murphy
#Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#3. Print first five and last three rows of dataframe
#A dataframe is the primary pandas structure of arranging data
#Import modules
import numpy as np
import pandas as pd

print("3. Print first five and last three rows of dataframe")
filename= 'irisdataset.txt'
#df is the globally accepted abbreviation for DataFrame
df=pd.read_csv(filename)



print (df.head())
#this linux command returns 5 as a default
print(df.tail(3))
#this time 3 is passed into the argument

