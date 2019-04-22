#22042019 Investigate the DataSet using sci-kit learn, the KNN algorithm
#using train_test_split, metrics and pyplot to produce a plot
#code verbatim from https://github.com/Msanjayds/Scikit-learn/blob/master/KNN%20on%20Iris%20Datset.ipynb
#This code is a good one to demonstrate how the various modules in sci-kit learn function
#iris data set is built into sc-kit learn due to it's popularity
from sklearn.datasets import load_iris
#rename the data set to iris
iris = load_iris()
type(iris)
print ("Predict with the KNN algorithm, then plot the relationship between K and testing accuracy") 
X = iris.data
y = iris.target

#train_test_split is a tool in the sci-kit learn library that splits
#data randomly into training and testing datasets.
from sklearn.model_selection import train_test_split
#test_size parameter decides the size of the data to be split 
#as the test dataset. This is given as a fraction 0.2 = 20% (80/20 is a common split in data science)
#either test_size or train_size is specfied (not both)
#random state is used as a random number generator, if it's not passed into the argument
#np.random will be used
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=17)
#import the KNeighbours classifier, it operates like a template
from sklearn.neighbors import KNeighborsClassifier
#the metrics module will allow for scoring functionality
from sklearn import metrics
k_range = range(1,10)
scores = {}
scores_list = []
for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        #fit the learning model with training data specified above
        knn.fit(X_train,y_train)
        #predict the response
        y_pred=knn.predict(X_test)
        scores[k] = metrics.accuracy_score(y_test,y_pred)
        scores_list.append(metrics.accuracy_score(y_test,y_pred))
print (scores)

import matplotlib.pyplot as plt

#plot the relationship between K and the testing accuracy
plt.plot(k_range,scores_list)
plt.xlabel('Value of K for kNN')
plt.ylabel('Testing Accuracy')
plt.show()

