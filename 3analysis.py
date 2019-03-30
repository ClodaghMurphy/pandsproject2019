#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM
#2. read text file into a dataframe
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

