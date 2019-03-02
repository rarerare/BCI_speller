from PIL import Image, ImageTk
import Tkinter as tk
import threading
from threading import Timer
import time
import random
faceNum=4
colorNum=4
interval_stimulus=1.0

num_trial=3*2*faceNum
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
    time.sleep(1.0)
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
        time.sleep(1.0)
        switchImg(faceImages[2*i], panelRight)
        switchImg(faceImages[2*i+1], panelLeft)

        stimuli.append(Stimulus(i, congruent, time.time()))
        time.sleep(0.5)
    panelRight.configure(image=TargetBlankImg)
    panelRight.image = TargetBlankImg
    panelLeft.configure(image=nonTargetBlankImg)
    panelLeft.image=nonTargetBlankImg
    printTimeStamps()

def displayColorImgs(stimuli, panelLeft, panelRight):
    time.sleep(1.0)
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
        time.sleep(1.0)
        switchImg(incongruentColorImages[2*i+random.choice([0,1])], panelRight)
        switchImg(congruentColorImages[i], panelLeft)
        

        stimuli.append(Stimulus(i, congruent, time.time()))
        time.sleep(0.5)
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






window.mainloop()





        