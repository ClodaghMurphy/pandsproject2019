#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM

#Import modules
import numpy as np
import pandas as pd

print("3. Print Index")
filename= 'irisdataset.txt'
#df is the globally accepted abbreviation for DataFrame
df=pd.read_csv(filename)

#returns information about the index, where it starts, stops and how it is incremented
print (df.index)


