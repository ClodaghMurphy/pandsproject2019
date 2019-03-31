#30032019 Investigate the DataSet Clodagh Murphy
#Joe James "Python: Pandas Tutorial | Intro to DataFrames"
#https://www.youtube.com/watch?v=e60ItwlZTKM
#4. Print Datatypes contained in the Table
#Import modules
import numpy as np
import pandas as pd

print("4. Print Datatypes contained in the Table")
filename= 'irisdataset.txt'
#df is the globally accepted abbreviation for DataFrame
df=pd.read_csv(filename)

print (df.dtypes)
#The df.dtypes command returned the numerical data as being "float64" data type, this is how
#pandas refers to floating point numbers.  The species of flower was classified as an object.


