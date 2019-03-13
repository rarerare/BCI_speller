import numpy as np
import matplotlib.pyplot as plt
import ast
from scipy.stats import kurtosis
"""
Created on Mon Mar 11 12:10:51 2019

@author: mayli
"""
 =============================================================================
 f=open("signal_data\signal03_11_2019__10_14_48.txt", "r")
 g=open("stimuli_data\stimuli03_11_2019__10_57_39.txt", "r")
 if f.mode == 'r':
     contents=f.read()
     l=ast.literal_eval(contents)
 if g.mode == 'r':
     content=g.read()
     gg=ast.literal_eval(content)
 
 #plt.plot([t[0] for t in l])
 aa=np.array(l)
 plt.plot([t[0] for t in aa])
 
 =============================================================================


a=[i for i,x in enumerate(bicycles) if x=='trek']
