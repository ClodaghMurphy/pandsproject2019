#31032019 Investigate the DataSet Clodagh Murphy
#Code adapted from Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#11. Assignment of New Values
#Import modules
import numpy as np
import pandas as pd

print("11. Assignment of Values")
dataset= 'irisdataset.txt'
df=pd.read_csv(dataset)

#Assign a value to a particular scalar variable
#A scalar value is associated with every point in a space
#This command will change the existing value to the one specified in the command
df.loc[87,['sepal length in cm']]=99
print (df.iloc[87:89])

#Assign a new field with a specific value to the dataframe called stem height in cm
#This doesn't change the orginal data, it is immutable
#Print out the first five rows, see also 3analysis.py
df['stem height in cm']=20
print(df.head())