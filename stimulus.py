
from PIL import Image, ImageTk
import Tkinter as tk
import threading
from threading import Timer
import time
import random
import mindwave



faceNum=4
colorNum=4
interval_stimulus=1.0
stimulus_duration=0.5

num_trial=3*2*faceNum

initial_sleep=1.0


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
    time.sleep(initial_sleep)
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

        stimuli.append(Stimulus(i, congruent, time.time()))
        time.sleep(stimulus_duration)
    panelRight.configure(image=TargetBlankImg)
    panelRight.image = TargetBlankImg
    panelLeft.configure(image=nonTargetBlankImg)
    panelLeft.image=nonTargetBlankImg
    printTimeStamps()

def displayColorImgs(stimuli, panelLeft, panelRight):
    time.sleep(2.0)
    time.sleep(initial_sleep)
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
        

        stimuli.append(Stimulus(i, congruent, time.time()))
        time.sleep(stimulus_duration)
    panelRight.configure(image=TargetBlankImg)
    panelRight.image = TargetBlankImg
    panelLeft.configure(image=nonTargetBlankImg)
    panelLeft.image=nonTargetBlankImg
    printTimeStamps()        
        
def printTimeStamps():
    for i in range(10):
        for s in stimuli:
            print(s.timeStamp)
            print(s.congruent)
        time.sleep(2.0)

def recordRaw():
    headset = mindwave.Headset('/dev/tty.MindWaveMobile-SerialPo', '625f')
    time.sleep(initial_sleep)

    headset.connect()
    signal=[]
    start_time=time.time()
    while True:
        v=headset.raw_value
        time.sleep(0.001)
        print(v,headset.poor_signal, headset.blink)
        signal.append(v)
        if time.time()>start_time+30:
            break

    
    f=open('signal.txt', 'w')
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





        