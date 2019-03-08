
from PIL import Image, ImageTk
import Tkinter as tk
import threading
from threading import Timer
import time
import random
import mindwave

from datetime import datetime
import sys
import os
if not os.path.exists('stimuli_data'):
    os.makedirs('stimuli_data')
if not os.path.exists('signal_data'):
    os.makedirs('signal_data')

faceNum=4
colorNum=4
interval_stimulus=1.0
stimulus_duration=0.5

num_trial=2*2*faceNum

initial_sleep=5.0
samp_rate=1000.0
samp_interval=1.0/samp_rate
record_duration=30.0




class Stimulus(object):
    """docstring for stimulus"""
    def __init__(self, imgI, congruent, timeStamp=-1):
        super(Stimulus, self).__init__()
        self.imgIndex = imgI
        self.timeStamp=timeStamp
        self.congruent=congruent
        


def switchImg(img, panel):
    panel.configure(image=img)
    panel.image = img
    


#def displayFaceImgs(stimuli, panelLeft):
#    time.sleep(2*initial_sleep)
#    for j in range(num_trial):
#        i=random.choice(range(faceNum))
#        congruent=random.choice([True, False])
#        #prompt=""
#        #if congruent:
#        #    prompt="non target"
#        #else:
#        #    prompt="  target  "
#        #panelRight.configure(image=TargetBlankImg)
#        #panelRight.image = TargetBlankImg
#        panelLeft.configure(image=blackBlankImg)
#        panelLeft.image=blackBlankImg
#        
#
#        #promptPanel.configure(text=prompt)
#        #promptPanel.text=prompt
#        time.sleep(interval_stimulus)
#        #switchImg(faceImages[2*i], panelRight)
#        #switchImg(faceImages[2*i+1], panelLeft)
#
#        #flashing=True
#        stimuli.append(Stimulus(i, congruent, time.time()))
#        time.sleep(stimulus_duration)
#    #panelRight.configure(image=TargetBlankImg)
#    #panelRight.image = TargetBlankImg
#    panelLeft.configure(image=blackBlankImg)
#    panelLeft.image=blackBlankImg
#    #flashing=False
#    printTimeStamps()

def displayColorImgs(stimuli, panelLeft):
    time.sleep(2*initial_sleep)


    
    for j in range(num_trial):
        i=random.choice(range(colorNum))
        congruent=random.choice([True, False])
       
        panelLeft.configure(image=blackBlankImg)
        panelLeft.image=blackBlankImg
        


        time.sleep(interval_stimulus)
        if congruent:
            nextImg=congruentColorImages[i]
        else:
            nextImg=incongruentColorImages[2*i+random.choice([0,1])]
        switchImg(nextImg, panelLeft)

        stimuli.append(Stimulus(i, congruent, time.time()))
        time.sleep(stimulus_duration)

    panelLeft.configure(image=blackBlankImg)
    panelLeft.image=blackBlankImg
    printTimeStamps()
      
        
def printTimeStamps():
    f=open('stimuli_data/stimuli'+dateTimeString+'.txt', 'w')
    f.write(str([(s.imgIndex, s.congruent, s.timeStamp) for s in stimuli])) 
    f.close()

def recordRaw():
    headset = mindwave.Headset('/dev/tty.MindWaveMobile-SerialPo', '625f')
    time.sleep(initial_sleep)
    headset.connect()
    signal=[]
    
    
    print("samp_interval"+str(samp_interval))

    start_time=time.time()
    
    for i in range(int(record_duration*samp_rate)):
        if (start_time+samp_interval*(i+100)-time.time())>0:
            time.sleep(start_time+samp_interval*(i+100)-time.time())
        else:
            print("skipped")

        v=headset.raw_value
        
        print(v,headset.poor_signal)
        signal.append((v, time.time()))

        


    #print("start-end"+str(time.time()-start_time))
    f=open('signal_data/signal'+dateTimeString+'.txt', 'w')
    f.write(str(signal))
    f.close()

window = tk.Tk()
faceImages=[]
congruentColorImages=[]
incongruentColorImages=[]
stimuli=[]


# load face images
for i in range(faceNum):
    invertImg=ImageTk.PhotoImage(Image.open("faceImg/InvertedFace"+str(i)+".jpg"))
    faceImages.append(invertImg)
    regularImg=ImageTk.PhotoImage(Image.open("faceImg/RegularFace"+str(i)+".jpg"))
    faceImages.append(regularImg)



#load color images
for i in range(1,colorNum+1):
    congruentImg=ImageTk.PhotoImage(Image.open("colorImg/Congruent"+str(i)+".jpg"))
    inCongruentImg1=ImageTk.PhotoImage(Image.open("colorImg/Incongruent"+str(i)+"_"+"1.jpg"))
    inCongruentImg2=ImageTk.PhotoImage(Image.open("colorImg/Incongruent"+str(i)+"_"+"2.jpg"))
    congruentColorImages.append(congruentImg)
    incongruentColorImages.append(inCongruentImg1)
    incongruentColorImages.append(inCongruentImg2)


blackBlankImg=ImageTk.PhotoImage(Image.open("blank_black.jpg"))
window.title("Face")
window.geometry("500x500")

panelLeft = tk.Label(window)
panelLeft.pack(side = "left", fill = "none", expand = "yes")
panelLeft.configure(image=blackBlankImg)
panelLeft.image=blackBlankImg




dateTimeString=datetime.now().strftime("%m_%d_%Y__%H_%M_%S")
displayThread=threading.Thread(target=displayColorImgs, args=(stimuli, panelLeft))
displayThread.start()


recordRawThread=threading.Thread(target=recordRaw)
recordRawThread.start()






window.mainloop()





        