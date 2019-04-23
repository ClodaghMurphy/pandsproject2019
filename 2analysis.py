#30032019 Investigate the DataSet Clodagh Murphy
#Code adapted from Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#2. Read text file into a dataframe
#A dataframe is the primary pandas structure of arranging data
#Import modules
import numpy as np
import pandas as pd

print("2. Read text file into a dataframe")
#import the dataset text file which is saved locally into pandas, rename it as dataset
dataset= 'irisdataset.txt'
#df is the globally accepted abbreviation for DataFrame
df=pd.read_csv(dataset)

print (df)
#Observations: i didn't have to give the dataset an index, the dataframe automatically did this
#A description appears on the bottom line i.e. [150 rows x 5 columns]
#I noticed numbering began on the second line of data.
#I removed the formatting that I had on the fields e.g.'petal width in cm','species', then the
#data appeared in the correct way, that is the dataframe recognised the first line to
#be classification and began numbering on the second. 
# Just one line of code brings in the data and sets it out in an easy to understand way. Very smart!