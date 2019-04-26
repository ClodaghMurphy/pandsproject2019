#31032019 Investigate the DataSet Clodagh Murphy
#Code adapted from Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#12. Rename fields 
#Import modules
import numpy as np
import pandas as pd

print("12. Rename fields ")
filename= 'irisdataset.txt'
df=pd.read_csv(filename)

#Rename the column called 'species' to 'type of iris'
#Print out the first five rows to demonstrate the change
df.rename(columns={'species': 'type of iris'}, inplace=True)
print(df.head())

#This is an easy way to change all the column names at once
#then, print out the first five rows to demonstrate
df.columns=['L sepal','W sepal','L petal','W petal','flower']
print(df.head())