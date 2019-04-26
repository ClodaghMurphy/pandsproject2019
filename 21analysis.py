#12042019 Investigate the DataSet
#Data Visualisation with pands and matplotlib functions
#verbatim from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

import matplotlib
import matplotlib.pyplot as plt
import pandas

#Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width which each
#species identified

dataset = pandas.read_csv('irisdataset.txt')
#plt.figure() this command appeared in the original
#code but I identified that it was responsible for an error
#that caused an extra, blank figure to appear.
#User Suever on stackoverflow advised on a similar query, I applied the solution to this problem with
#the desired effect.
#https://stackoverflow.com/questions/43237079/why-plt-show-shows-one-extra-blank-figure
#Unfortunately the same solution did not work for 20analysis.py
fig,ax=plt.subplots(1,2,figsize=(21, 10))
#create new datasets from the original that contain data about one particular species
setosa=dataset[dataset['species']=='Iris-setosa']
versicolor =dataset[dataset['species']=='Iris-versicolor']
virginica =dataset[dataset['species']=='Iris-virginica']                                                            
#Assign sepal data to one plot
setosa.plot(x="sepal length in cm", y="sepal width in cm", kind="scatter",ax=ax[0],label='setosa',color='y')
versicolor.plot(x="sepal length in cm",y="sepal width in cm",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal length in cm", y="sepal width in cm", kind="scatter", ax=ax[0], label='virginica', color='g')
#Assign petal data to the other plot
setosa.plot(x="petal length in cm", y="petal width in cm", kind="scatter",ax=ax[1],label='setosa',color='y')
versicolor.plot(x="petal length in cm",y="petal width in cm",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal length in cm", y="petal width in cm", kind="scatter", ax=ax[1], label='virginica', color='g')

ax[0].set(title='Sepal Comparison ', ylabel='sepal-width')
ax[1].set(title='Petal Comparison',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()

