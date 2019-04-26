#31032019 Investigate the DataSet Clodagh Murphy
#Code adapted from Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#13. Write the dataframe to a csv or xls file 
#Import modules
import numpy as np
import pandas as pd

print("13. Write the dataframe to a csv and xls file ")
dataset= 'irisdataset.txt'
df=pd.read_csv(dataset)

df.to_csv('irisdf.csv')
df.to_excel('irisdf1.xls')

#There is no outut on the command line
#the new files are saved in the same place as the python script