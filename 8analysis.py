#30032019 Investigate the DataSet Clodagh Murphy
#Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#8. Print a Statistical Summary of the Iris DataSet
#Import modules
import numpy as np
import pandas as pd

print("8. Print a Statistical Summary of the Iris DataSet")
dataset= 'irisdataset.txt'
df=pd.read_csv(dataset)

#Print summary of statistics for numerical columns
#Count, mean, standard deviation, minimum, maximum, 25/50/75 percentiles
#That is a very useful feature.

print (df.describe())

#I redefined the data frame to just be the 'species' column which contains objects
#and not numerical data, this gave me a different set of results - more meta!
df=(df['species'])
print (df.describe())

