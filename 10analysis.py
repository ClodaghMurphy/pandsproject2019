#30032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM

#Import modules
import numpy as np
import pandas as pd

print("10. Slices of Data")
filename= 'irisdataset.txt'
df=pd.read_csv(filename)

#Print only a "Slice" of the dataset, in this instance the column 'sepal length in cm'
#square brackets operator is used
print (df['sepal length in cm'])

#Print only a "Slice" of the dataset, use square brackets to indicate the contents of rows 50-60
print (df[50:60])

#Pass column names into double squarebrackets to print multiple columns listed
print(df[['sepal length in cm','petal length in cm']])

#Print the data in two columns, the loc (location) command accepts up to four parameters
#e.g. 2 columns and 2 row parameters
#This example doesn't set row parameters, the colon indicates that all rows are required
#A parameter (even a null one) must be entered in order for the command to execute
print(df.loc[:,['sepal length in cm','petal length in cm']])

#This example of loc indicates specific rows in the range 70 to 80 are required
print(df.loc[70:80,['sepal length in cm','petal length in cm']])

#loc can be used to return a scalar variable, an important concept in data analysis.
# A scalar value is associated with every point in a space
#40 is the index of the row and 'sepal length in cm' is the column
print(df.loc[40,['sepal length in cm']])

#iloc provides index location.The index of the rows and columns are used instead of titles where
#they exist
print(df.iloc[40:50,[1,2]])
