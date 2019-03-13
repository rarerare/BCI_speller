import numpy as np
import matplotlib.pyplot as plt
import ast
from scipy.stats import kurtosis

"""
purpose: parse raw data/label file, return data as numpy array
"""

def parse_file(dataFileName):
    f=open(dataFileName)
    strL=f.read()
    l=ast.literal_eval(strL)
    return np.array(l)

def plotData(data):
    plt.plot([x[0] for x in data])
    plt.plot([x[2] for x in data])#poor_signal
    return

def plotData2(data):
    for x in data:
        plt.plot([i[0] for i in x])
    return

#Test
dataFileName='signal_data\signal03_11_2019__10_43_51.txt'
postData=parse_file(dataFileName)
plotData(postData)
print(len(postData)/30)
 
f="signal_data\signal03_11_2019__10_57_39.txt" #signal data
g="stimuli_data\stimuli03_11_2019__10_57_39.txt" #stimuli stamp

#signalFile format: (outputlevel, timestamp, quality)
#stimuliFile format: (pictureIndex,condition,timestamp)
#output format: 2d tuple with each elment as a sample, each sample; scope is in seconds
#def sync( signalFile, stimuliFile, scope):
#    f=parse_file(signalFile)
#    g=parse_file(stimuliFile)
#    out=[]
#    temp=[]
#    for i in g:
#        temp=[]
#        for j in f:
#            if j[1]>i[2] and j[1]<i[2]+scope:
#                temp.append(j)
#        out.append(temp)
#    return out
#
#res=sync(f,g,1.5)
#plotData(res[7])
#
#def getLabel(stimuliFile):
#    out=[]
#    g=parse_file(stimuliFile)
#    for x in g:
#       out.append(int(x[1]))
#    return out
#
#print(getLabel(g)) 


