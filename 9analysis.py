#30032019 Investigate the DataSet Clodagh Murphy
#Code adapted from Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#9. Sort the records by descending value of petal length in cm
#Import modules
import numpy as np
import pandas as pd

print("9. Sort the records by descending value of petal length in cm")
dataset= 'irisdataset.txt'
df=pd.read_csv(dataset)

#Sort the records by value of 'petal length in cm'

print (df.sort_values('petal length in cm', ascending=False))

