#12042019 Investigate the DataSet
#Data Visualisation with pands and matplotlib functions
#verbatim from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

import matplotlib
import matplotlib.pyplot as plt
import pandas

#Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width

dataset = pandas.read_csv('irisdataset.txt')
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(17, 9))
dataset.plot(x="sepal length in cm",y="sepal width in cm",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
dataset.plot(x="petal length in cm",y="petal width in cm",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal Comparison ', ylabel='sepal-width')
ax[1].set(title='Petal Comparison',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()
#plt.close()
