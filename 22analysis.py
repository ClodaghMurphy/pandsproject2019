#12042019 Investigate the DataSet using pandas
#Data Visualisation with pandas
#verbatim from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
import pandas

#Creating a new data set and Sorting the records by species and column values 

dataset = pandas.read_csv('irisdataset.txt')
#this is another example of passing arguments into the dataset commmand to
#use data from the original dataset to create new datasets
#== double equals, I utilised this equals operator in the first problem set assignment
setosa=dataset[dataset['species']=='Iris-setosa']
versicolor =dataset[dataset['species']=='Iris-versicolor']
virginica =dataset[dataset['species']=='Iris-virginica']     


print ('This is a list of setosa specific data sorted by petal length in cm in descending value')
print (setosa.sort_values('petal length in cm', ascending=False))
print ('This is a list of versicolor specific data sorted by petal width in cm in ascending value')
print (versicolor.sort_values('petal width in cm', ascending=True))
print ('This is a list of virginica specific data sorted by sepal width in cm in descending value')
print (virginica.sort_values('sepal width in cm', ascending=False))
