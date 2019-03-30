#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM
#2. read text file into a dataframe
#A dataframe is the primary pandas structure of arranging data
#Import modules
import numpy as np
import pandas as pd

print("2. read text file into a dataframe")
filename= 'irisdataset.txt'
df=pd.read_csv(filename)

print (df)
#Observations: i didn't have to give the dataset an index, the dataframe automatically did this
#A description appears on the bottom line i.e. [150 rows x 5 columns]
#I notice numbering began on the second line of data so this oversight needs to be rectified.