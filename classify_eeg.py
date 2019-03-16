import raw_signal_processing as rsp
import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import bandFilter
fs=1000
signalDirName='signal_data'
stimuliDirName='stimuli_data'
signalFileNames=[]
stimuliFileNames=[]

#for filename in os.listdir(signalDirName):
#        if filename.startswith('signal') and filename.endswith('.txt'):
#            print(filename)

if not os.path.isfile('trials_signal.npy'):
    for filename in os.listdir(signalDirName):
        if filename.startswith('signal') and filename.endswith('.txt'):
            signalFileNames.append(filename)
            stimuliFileNames.append('stimuli'+filename[6:])

    #print(len(signalFileNames))
    #print(len(stimuliFileNames))

    trials_signal=[]
    trials_stimuli=[]
    for sigFN, stiFN in zip(signalFileNames, stimuliFileNames):
        
        file_trial_signal, file_trial_stimuli=rsp.sync(signalDirName+'/'+sigFN, stimuliDirName+'/'+stiFN, 0.0, 1.5)
        trials_signal=trials_signal+file_trial_signal
        trials_stimuli=trials_stimuli+file_trial_stimuli
        #print(trials_stimuli)


    
    #for stiFN in stimuliFileNames:
     #   trials_stimuli=trials_stimuli+rsp.getLabel(stimuliDirName+'/'+stiFN)

    #print(np.array(trials_signal).shape)
    #print( np.array(trials_stimuli).shape)

    np.save('trials_signal.npy', np.array(trials_signal))
    np.save('trials_stimuli.npy', np.array(trials_stimuli))

trials_signal=np.load('trials_signal.npy')
print(trials_signal.shape)
trials_rawVal=[]
trials_bandPower=[]
for trial in trials_signal:
    raw=[x[0] for x in trial]

    
    raw=bandFilter.butter_bandpass_filter(np.array(raw), 0.5, 30, fs, order = 2)
    trials_rawVal.append(raw)
    f,p= bandFilter.bandPower(raw)
    trials_bandPower.append(p[1:60])

trials_rawVal=np.array(trials_rawVal)
print(trials_rawVal.shape)
trials_stimuli=np.load('trials_stimuli.npy')
print(trials_stimuli.shape)
#sigOne=[]
#
#for i in range(560, 576):
#    sigOne=sigOne+trials_rawVal[i].tolist()
#
##
##
#plt.plot(sigOne)
#plt.show()
#for t in trials_rawVal:
#    t=bandFilter.butter_bandpass_filter(np.array(t), 0.5, 30, fs, order = 2)
#    plt.plot(t)
#plt.show()
congruent_sigs=[]
incongruent_sigs=[]


for sig, sti in zip(trials_rawVal, trials_stimuli):
    if sti:
        congruent_sigs.append(sig)
    else:
        incongruent_sigs.append(sig)

#for s in congruent_sigs:
#    plt.plot(s)
#plt.show()
clf_lsqrs = LinearDiscriminantAnalysis(solver = 'lsqr',  shrinkage = 'auto').fit(trials_rawVal[:80], trials_stimuli[:80])
correct_count=0
for b,s in zip(trials_rawVal[80:], trials_stimuli[80:]):
    predict=clf_lsqrs.predict([b])
    if predict[0]==s:
        correct_count+=1

print(correct_count)

correct_count=0
clf = SVC(gamma='auto')
clf.fit(trials_bandPower[:500], trials_stimuli[:500])
for b,s in zip(trials_bandPower, trials_stimuli):
    predict=clf.predict([b])
    if predict[0]==s:
        correct_count+=1
print(correct_count)        

score_lsqrs = cross_val_score(clf_lsqrs.fit(trials_rawVal, trials_stimuli), trials_rawVal, trials_stimuli, cv = 5)

# We will print out the mean score
print("solver = lsqr  accuracy: " + str(np.mean(score_lsqrs)))


