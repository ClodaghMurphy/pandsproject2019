#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM

#Import modules
import numpy as np
import pandas as pd

print("7. Print Values")
filename= 'irisdataset.txt'
df=pd.read_csv(filename)

#returns list of values contained in the dataframe
print (df.values)

