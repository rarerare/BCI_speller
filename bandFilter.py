from scipy.signal import butter, sosfiltfilt, sosfreqz
import numpy as np
import scipy
################################################################################
# Credit for these functions goes to 'WarrenWeckesser'
# https://scipy-cookbook.readthedocs.io/items/ButterworthBandpass.html

def butter_bandpass(lowcut, highcut, fs, order = 2):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog = False, btype = 'band', output = 'sos')
        return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order = 2):
        sos = butter_bandpass(lowcut, highcut, fs, order = order)
        y = sosfiltfilt(sos, data)
        return y




##############################################################################

fs=1000

deltaCuts=[0.1, 4]
thetaCuts=[4,7]
alphaCuts=[8,12]
muCuts=[8,13]
betaCuts=[12,30]
gammaCuts=[30,100]


###################################
def shiftMeanTo0(data):
    m=np.mean(data)
    return [i -m for i in data]


def bandPower(signal):
    frequency, pd=scipy.signal.welch(signal, fs,nperseg=2000)
    return frequency, pd

if __name__ == "__main__":
    import ast
    import matplotlib.pyplot as plt
    f=open('signal_data/signal03_11_2019__10_57_39.txt')
    strL=f.read()
    #print(strL)
    l=ast.literal_eval(strL)
    
    #print(len(l))
    signal=[t[0] for t in l]
    signal=shiftMeanTo0(signal)
    alphaBand=butter_bandpass_filter(np.array(signal), gammaCuts[0], gammaCuts[1], fs)
    
    #plt.plot(signal)
    #plt.plot(alphaBand)

    f, p=bandPower=bandPower(signal)
    print(f)
    plt.plot(f[8:100],p[8:100])
    plt.show()




