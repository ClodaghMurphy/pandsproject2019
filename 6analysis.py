#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM

#Import modules
import numpy as np
import pandas as pd

print("6. Print Columns")
filename= 'irisdataset.txt'
#df is the globally accepted abbreviation for DataFrame
df=pd.read_csv(filename)

#returns list of column names

print (df.columns)


