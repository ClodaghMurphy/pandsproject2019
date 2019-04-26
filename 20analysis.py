#12042019 Investigate the DataSet
#Data Visualisation with pands and matplotlib functions
#adapted from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

import matplotlib
import matplotlib.pyplot as plt
import pandas

#Plotting Scatterplot Petal Length vs Petal Width & Sepal Length vs Sepal width

dataset = pandas.read_csv('irisdataset.txt')
#According to https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html
#fig, ax = plt.sublots() creates just a figure and only one subplot
#ax can be either a single Axes object or an array of Axes objects if more than one subplot was created. 
fig,ax=plt.subplots(1,2,figsize=(21, 10))
fig,ax=plt.subplots(1,2,figsize=(17, 9))

dataset.plot(x="sepal length in cm",y="sepal width in cm",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
dataset.plot(x="petal length in cm",y="petal width in cm",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal Comparison ', ylabel='sepal-width')
ax[1].set(title='Petal Comparison',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()

plt.show()
#While this plot does not separate the different species, it's an interesting image to
#view and recognise how some petals measurements are very obviously distinguishable
