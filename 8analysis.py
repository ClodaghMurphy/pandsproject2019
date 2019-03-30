#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM

#Import modules
import numpy as np
import pandas as pd

print("8. Print a Statistical Summary of the Iris DataSet")
filename= 'irisdataset.txt'
df=pd.read_csv(filename)

#Print statistical summary of the data
#Count, mean, standard deviation, minimum, maximum, 25/50/75 percentiles

print (df.describe())

