# Pan and Xian's code
import numpy as np
import matplotlib.pyplot as plt
import ast
from scipy.stats import kurtosis




# From Jiuqi Xian's code
"""
purpose: parse raw data/label file, return data as numpy array
"""
dataFileName=
def parse_file(dataFileName):
    f=open(dataFileName)
    strL=f.read()
    l=ast.literal_eval(strL)
    return np.array(l)

"""
purpose: find the indeces of trails that possibly contaminated by eyeblinks
"""
def eyeblink_identifier(brainwave_vec, window_interval,num_of_trials, moving_step, rejection_std):
    kurtosis_vec = np.array([])
    idx =0
    while (idx < brainwave_vec.size-window_interval):
        np.append(kurtosis, kurtosis(brainwave_vec[idx:idx+window_interval]))
        idx += moving_step
    kurtosis_thres = np.mean(kurtosis_vec)+ rejection_std*np.std(kurtosis_vec)
    bad_kurtosis_index = kurtosis_vec > kurtosis_thres
    
    num_windows_per_trial = (brainwave_vec.size-window_interval)/ moving_step+1
    bad_trial_index = []
    
    for i in range(0,kurtosis_vec.size):
        if (bad_kurtosis_index[i] == True):
            bad_train_index.append(np.floor(i/(1.0*num_windows_pertrial)))
    
    return np.unique(bad_trial_index)

"""
purpose: find the indices of trials that have bad connection
"""

def bad_connection_identifier(stimuli_per_trial,num_of_trials, connection_quality_vec,rejection_rate):
    bad_trial_index =[]
    for i in range(0, num_of_trials-1):
        bad_sum = 0
        for j in range(i*stimuli_per_trial,(i+1)*stimuli_per_trial):
            if (connection_quality_vec[j] > tres):
                bad_sum += 1
        if (bad_sum/(1.0)*stimuli_per_trial > rejection_rate):
            bad_trial_index.append(i)
            
    return np.array(bad_trial_index)
            
    
     
# From Hongyi Pan's code    


f="signal_data\signal03_11_2019__10_57_39.txt" #signal data
g="stimuli_data\stimuli03_11_2019__10_57_39.txt" #stimuli stamp

#signalFile format: (outputlevel, timestamp, quality)
#stimuliFile format: (pictureIndex,condition,timestamp)
#output format: 2d tuple with each elment as a sample, each sample a point of signalFile format
#scopePre and scopePost are the seconds before/after included in the sample
def sync( signalFile, stimuliFile, scopePre, scopePost):
    f=parse_file(signalFile)
    g=parse_file(stimuliFile)
    out=[]
    temp=[]
    for i in g:
        temp=[]
        for j in f:
            if j[1]>i[2]+scopePre and j[1]<i[2]+scopePost:
                temp.append(j)
        out.append(temp)
    return out

#Test
res=sync(f,g,-0.2,1)
plotData(res[0])

def getLabel(stimuliFile):
    out=[]
    g=parse_file(stimuliFile)
    for x in g:
       out.append(int(x[1]))
    return out

#Test
print(getLabel(g))