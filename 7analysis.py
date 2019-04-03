#30032019 Investigate the DataSet Clodagh Murphy
#Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#7. Print Values contained in the dataframe
#Import modules
import numpy as np
import pandas as pd

print("7. Print Values")
dataset= 'irisdataset.txt'
df=pd.read_csv(dataset)

#returns list of values (contents) of the dataframe
print (df.values)

