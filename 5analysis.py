#30032019 Investigate the DataSet Clodagh Murphy
#Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#3. Print Index
#Import modules
import numpy as np
import pandas as pd

print("3. Print Index")
dataset= 'irisdataset.txt'
#df is the globally accepted abbreviation for DataFrame
df=pd.read_csv(dataset)

#returns information about the index, where it starts, stops and how it is incremented
print (df.index)


