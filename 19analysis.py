#12042019 Investigate the DataSet
#Experimenting with pandas functions
#Adapted from
# https://stackoverflow.com/questions/33034243/calculating-the-mean-and-std-on-excel-file-using-python
#Import pandas module
import pandas
#
#The standard deviation is amount of variability (or spread) 
#among the numbers in a data set, that is the standard (or typical) 
# amount of deviation (or distance) from the mean
#https://wiki.kidzsearch.com/wiki/Standard_deviation

dataset = pandas.read_csv('irisdataset.txt')
print(" 'std' calculates and displays the standard deviation in each column")
print(dataset.std())


