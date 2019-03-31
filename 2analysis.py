#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM
#2. read text file into a dataframe
#A dataframe is the primary pandas structure of arranging data
#Import modules
import numpy as np
import pandas as pd

print("2. read text file into a dataframe")
filename= 'irisdataset.txt'
#df is the globally accepted abbreviation for DataFrame
df=pd.read_csv(filename)

print (df)
#Observations: i didn't have to give the dataset an index, the dataframe automatically did this
#A description appears on the bottom line i.e. [150 rows x 5 columns]
#I notice numbering began on the second line of data so this oversight needs to be rectified.
#I removed the formatting that I had on the fields e.g.'petal width in cm','species', then the
#data appeared in the correct way, that is the dataframe recognised the first line to
#be classification and began numbering on the second. 
# Just one line of code brings in the data and sets it out in an easy to understand way. Very smart!