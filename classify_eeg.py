import raw_signal_processing as rsp
import os
import numpy as np
import matplotlib.pyplot as plt

 
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
        
        file_trial_signal, file_trial_stimuli=rsp.sync(signalDirName+'/'+sigFN, stimuliDirName+'/'+stiFN, 0, 1.5)
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
for trial in trials_signal:
    trials_rawVal.append([x[0] for x in trial])
    
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


