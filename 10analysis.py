#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM

#Import modules
import numpy as np
import pandas as pd

print("10. Slices of Data")
filename= 'irisdataset.txt'
df=pd.read_csv(filename)

#Print only a "Slice" of the dataset, in this instance the column 'sepal length in cm'
print (df['sepal length in cm'])
#Print only a "Slice" of the dataset, in this instance rows 50-60
print (df[50:60])
