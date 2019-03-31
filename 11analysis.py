#31032019 Investigate the DataSet
#https://www.youtube.com/watch?v=e60ItwlZTKM

#Import modules
import numpy as np
import pandas as pd

print("11. Assignment of Values")
filename= 'irisdataset.txt'
df=pd.read_csv(filename)

#Print 
df.loc[87,['sepal length in cm']]=6.5
print (df.iloc[87:95])