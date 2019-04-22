#22042019 Investigate the DataSet using sci-kit learn
#code verbatim from https://www.youtube.com/watch?v=hd1W4CyPX58

#iris data set is built into sc-kit learn due to it's popularity
from sklearn.datasets import load_iris
#rename the data set to iris
iris = load_iris()
type(iris)
print ("Using scikit-learn commands to print data, feature names, target and target names from the Iris dataset")
print (iris.data)
#scikit uses the term "feature" for the objects that the data contains information about 
#e.g. the sepal width is a feature.  This is machine learning terminology - each column is a feature.
print (iris.feature_names)
#the "target" means the outcome of what the dataset predicts.
#targets must be numeric (not a string) the target represents the different iris types in this format: 0,1,2
#the features and target data must be kept separate when using scikit learn
print (iris.target)
#what the target names are in string format
print (iris.target_names)

