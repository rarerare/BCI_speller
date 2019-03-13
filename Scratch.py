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

#Test
dataFileName='signal_data\signal03_11_2019__10_43_51.txt'
postData=parse_file(dataFileName)
#plotData(postData)
 
f="signal_data\signal03_11_2019__10_57_39.txt" #signal data
g="stimuli_data\stimuli03_11_2019__10_57_39.txt" #stimuli stamp

#signalFile format: (outputlevel, timestamp, quality)
#stimuliFile format: (pictureIndex,condition,timestamp)
#output format:

def sync( signalFile, stimuliFile, scope):
    f=parse_file(signalFile)
    g=parse_file(stimuliFile)
    out=[]
    for i in g:
        #out.append(g[counter])
        for j in f:
            if j[1]>i[2] and j[1]<i[2]+scope:
                out.append(j)
        
    return out


res=sync(f,g,1.5)
ff=parse_file(f)
print(len(ff))
print(len(res))
plotData(res)
   