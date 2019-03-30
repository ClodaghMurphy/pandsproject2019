#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM

#Import modules
import numpy as np
import pandas as pd

print("9. Sort the records by descending value of petal length in cm")
filename= 'irisdataset.txt'
df=pd.read_csv(filename)

#Sort the records by value of 'petal length in cm'

print (df.sort_values('petal length in cm', ascending=False))

