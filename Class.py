import statistics
import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df=pd.read_csv("data.csv")
data=df["temp"]

# fig=ff.create_distplot([data],["average"])
# fig.show()

# mean=statistics.mean(data)
# population_standard_deviation=statistics.stdev(data)
# mode=statistics.mode(data)
# median=statistics.median(data)

# print("mean is :"+str(mean))
# print("mode is :"+str(mode))
# print("median is :"+str(median))
# print("standard diviation is :"+str(population_standard_deviation))

# dataSet=[]
# for i in range(0,100):
#     randomIndex=random.randint(0,len(data))
#     value=data[randomIndex]
#     dataSet.append(value)

# mean=statistics.mean(dataSet)
# population_standard_deviation=statistics.stdev(dataSet)
# mode=statistics.mode(dataSet)
# median=statistics.median(dataSet)

# print("sample mean is :"+str(mean))
# print("sample mode is :"+str(mode))
# print("sample median is :"+str(median))
# print("sample standard diviation is :"+str(population_standard_deviation))

def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)

    mean=statistics.mean(dataSet)
    
    return mean

def sampling():
    meanList=[]
    for i in range(0,1000):
        setOfMean=randomSetOfMean(100)
        meanList.append(setOfMean)
    
    fig=ff.create_distplot([meanList],["temp"])
    fig.show()

    samplingMean=statistics.mean(meanList)
    samplingStdev=statistics.stdev(meanList)

    print("sampling mean is :"+str(samplingMean))
    print("sampling Stdev is :"+str(samplingStdev)) 

sampling()

