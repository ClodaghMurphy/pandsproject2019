#30032019 Investigate the DataSet Clodagh Murphy
#Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#6. Print Columns
#Import modules
import numpy as np
import pandas as pd

print("6. Print Columns")
dataset= 'irisdataset.txt'
#df is the globally accepted abbreviation for DataFrame
df=pd.read_csv(dataset)

#returns list of column names

print (df.columns)


