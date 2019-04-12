1. I read online articles/watched youtube videos on the subject and wrote a summary, see "Summary of Initial Research" document
2. I started a list of references in the README to populate over the course of the project.
3. I downloaded the Data Set (1999 version) and Data Set Description from  http://archive.ics.uci.edu/ml/datasets/Iris
4. I'm a visual person so I also downloaded and saved images of the three types of iris...however they are
    still very difficult to distinguish visually!
5. I read about pandas - the open source python library that provides high level data analysis tools. 
    It runs on top of numPy - a foundational data structure for many python libraries.   
6. I used python code to familiarise myself with pandas and how it can be used to investigate the iris dataset.  
7.I learned that pandas is an efficient tool that displays/arranges the data in a meaningful way usually with just one command.
8.The df.dtypes command returned the numerical data as being "float64" data type, this is how
pandas refers to floating point numbers.  The species of flower was classified as an object.
sepal length in cm    float64
species                object
9. A few more commands from a medium.com user
10. Box plots get the name from the box in the middle of the diagram and are a way to display numerical data via their quartiles. 
In the figure that is rendered:
- the minimum is represented by the lowermost line (a "whisker")
- the maximum value is the uppermost line (a "whisker")
- the lowermost end of each box is quartile 1, the uppermost represents quartile 3
- the second quartile (the median) is the line inside the box.
- the circles that appear on the plot for "sepal width in cm" indicate data that is outside the median, unusual recordings compared to the majority of the data
- a compact box indicates less variation in the values, as shown in the data relating to iris sepals.
I have programs to display univariate and multivariate versions of boxplots
11. Histograms represent one variable in a visualisation (different from a bar chart which relates two!). 
It is a very simple command to create a histogram.
12. The analysis so far is considered to be exploring the data using "descriptive statistics", it's a starting point to help understand
the data by summarising what you have (as opposed to making predictions or inferential statistics). Important statistics to
set out are what is normal (central) and what is at the outermost ranges (variability, spread, deviation).
A box plot can provide a lot of these statistics in one image.

.
13. MY INVESTIGATIONS INTO THE DATA SET
Ben Hamner  https://www.kaggle.com/benhamner/sepal-width-vs-length
demonstrates with a scatter graph that the setosa species is "linearly separable" from the other two in the data set.  
In the graph all 50 setosa flowers can be seen lying distinctly separate, the other 100 flowers merge.
14 The standard deviation is a measurement statisticians use for the amount of variability (or spread) 
among the numbers in a data set. As the term implies, a standard deviation is a standard (or typical) amount of 
deviation (or distance) from the average (or mean, as statisticians like to call it).
15 bar Graph VS Histogram
16 outliers demonstrated in plot or histogram
17 Having analysed the data set, now it's time to try and draw some conclusions.  Petals are the colourful part of a flower
that surround the reproductive elements, the sepals (usually green but not in this instance!) protect the bud and support the petals
after budding. Comparison of "like with like" should provide more meaningful results.


    Pandas Analysis | Description
    ------------ | -------------
    Analysis 1 | Load a segment of hardcoded data into a dataframe
    Analysis 2 | Read text file into a dataframe
