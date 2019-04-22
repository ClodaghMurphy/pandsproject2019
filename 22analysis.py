#12042019 Investigate the DataSet using pandas
#Data Visualisation with pandas
#verbatim from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
import pandas

#Sorting the records by species and column values 

dataset = pandas.read_csv('irisdataset.txt')

setosa=dataset[dataset['species']=='Iris-setosa']
versicolor =dataset[dataset['species']=='Iris-versicolor']
virginica =dataset[dataset['species']=='Iris-virginica']     


print ('This is a list of setosa data sorted by petal length in cm in descending value')
print (setosa.sort_values('petal length in cm', ascending=False))
print ('This is a list of versicolor data sorted by petal width in cm in ascending value')
print (versicolor.sort_values('petal width in cm', ascending=True))
print ('This is a list of virginica data sorted by sepal width in cm in descending value')
print (virginica.sort_values('sepal width in cm', ascending=False))
