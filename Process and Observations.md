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
11. Histograms represent one variable in a visualisation (different from a bar chart which relates two!). 
It is a very simple command to create a histogram.




    Pandas Analysis | Description
    ------------ | -------------
    Analysis 1 | Load a segment of hardcoded data into a dataframe
    Analysis 2 | Read text file into a dataframe
