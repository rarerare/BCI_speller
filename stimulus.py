
from PIL import Image, ImageTk
import Tkinter as tk
import threading
from threading import Timer
import time
import random
import mindwave

from datetime import datetime
import sys

faceNum=4
colorNum=4
interval_stimulus=1.0
stimulus_duration=0.5

num_trial=2*2*faceNum

initial_sleep=5.0
samp_rate=1000.0
samp_interval=1.0/samp_rate
record_duration=30.0

#flashing=False



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
    


def displayFaceImgs(stimuli, panelLeft, panelRight):
    time.sleep(2*initial_sleep)
    dateTimeString=datetime.now().strftime("%m_%d_%Y__%H_%M_%S")
    for j in range(num_trial):
        i=random.choice(range(faceNum))
        congruent=random.choice([True, False])
        prompt=""
        if congruent:
            prompt="non target"
        else:
            prompt="  target  "
        panelRight.configure(image=TargetBlankImg)
        panelRight.image = TargetBlankImg
        panelLeft.configure(image=nonTargetBlankImg)
        panelLeft.image=nonTargetBlankImg
        

        promptPanel.configure(text=prompt)
        promptPanel.text=prompt
        time.sleep(interval_stimulus)
        switchImg(faceImages[2*i], panelRight)
        switchImg(faceImages[2*i+1], panelLeft)

        #flashing=True
        stimuli.append(Stimulus(i, congruent, time.time()))
        time.sleep(stimulus_duration)
    panelRight.configure(image=TargetBlankImg)
    panelRight.image = TargetBlankImg
    panelLeft.configure(image=nonTargetBlankImg)
    panelLeft.image=nonTargetBlankImg
    #flashing=False
    printTimeStamps()

def displayColorImgs(stimuli, panelLeft, panelRight):
    time.sleep(2*initial_sleep)


    dateTimeString=datetime.now().strftime("%m_%d_%Y__%H_%M_%S")
    for j in range(num_trial):
        i=random.choice(range(colorNum))
        congruent=random.choice([True, False])
        prompt=""
        if congruent:
            prompt="non target"
        else:
            prompt="  target  "
        panelRight.configure(image=TargetBlankImg)
        panelRight.image = TargetBlankImg
        panelLeft.configure(image=nonTargetBlankImg)
        panelLeft.image=nonTargetBlankImg
        

        promptPanel.configure(text=prompt)
        promptPanel.text=prompt
        time.sleep(interval_stimulus)
        switchImg(incongruentColorImages[2*i+random.choice([0,1])], panelRight)
        switchImg(congruentColorImages[i], panelLeft)
        #flashing=True

        stimuli.append(Stimulus(i, congruent, time.time()))
        time.sleep(stimulus_duration)
    panelRight.configure(image=TargetBlankImg)
    panelRight.image = TargetBlankImg
    panelLeft.configure(image=nonTargetBlankImg)
    panelLeft.image=nonTargetBlankImg
    #flashing=False
    printTimeStamps()
      
        
def printTimeStamps():
    f=open('stimuli_data/stimuli'+dateTimeString+'.txt', 'w')
    f.write(str([(s.imgIndex, s.congruent, s.timeStamp) for s in stimuli])) 
    f.close()

def recordRaw():
    headset = mindwave.Headset('/dev/tty.MindWaveMobile-SerialPo', '625f')
    time.sleep(initial_sleep)
    dateTimeString=datetime.now().strftime("%m_%d_%Y__%H_%M_%S")
    headset.connect()
    signal=[]
    
    
    print("samp_interval"+str(samp_interval))
    #time_prev=time.time()
    #time_next=time.time()
    start_time=time.time()
    
    for i in range(int(record_duration*samp_rate)):
        if (start_time+samp_interval*(i+100)-time.time())>0:
            time.sleep(start_time+samp_interval*(i+100)-time.time())
        else:
            print("skipped")
        #time_prev=time_next
        v=headset.raw_value
        
        print(v,headset.poor_signal)
        signal.append((v, time.time()))
        #time_next=time.time()
        #print("time_prev"+str(time_prev)+"time_next"+str(time_next))
        #print ("sleep time"+str(samp_interval-(time_next-time_prev)))
        

        
        #if time.time()>start_time+30:
         #   break

    #print("start-end"+str(time.time()-start_time))
    f=open('signal_data/signal'+dateTimeString+'.txt', 'w')
    f.write(str(signal))
    #f.write("start time:"+str(start_time))
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

nonTargetBlankImg=ImageTk.PhotoImage(Image.open("NonTargetBlank.png"))
TargetBlankImg=ImageTk.PhotoImage(Image.open("TargetBlank.png"))

window.title("Face")
window.geometry("1200x600")
promptPanel=tk.Label(text="prompt")
promptPanel.pack(side="top", fill="none", expand="yes")
panelLeft = tk.Label(window)
panelLeft.pack(side = "left", fill = "none", expand = "yes")
panelLeft.configure(image=nonTargetBlankImg)
panelLeft.image=nonTargetBlankImg

panelRight = tk.Label(window)
panelRight.pack(side = "right", fill = "none", expand = "yes")
panelRight.configure(image=TargetBlankImg)
panelRight.image=TargetBlankImg



#displayThread=threading.Thread(target=displayFaceImgs, args=(stimuli, panelLeft, panelRight))
#displayThread.start()

displayThread=threading.Thread(target=displayColorImgs, args=(stimuli, panelLeft, panelRight))
displayThread.start()
#printTimeThread=threading.Thread(target=printTimeStamps)
#printTimeThread.start()

recordRawThread=threading.Thread(target=recordRaw)
recordRawThread.start()






window.mainloop()





        