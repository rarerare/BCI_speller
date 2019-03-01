from PIL import Image, ImageTk
import Tkinter as tk
import threading
from threading import Timer
import time

maxIndex=3
interval_stimulus=1.0

class Stimulus(object):
    """docstring for stimulus"""
    def __init__(self, imgI, timeStamp=-1):
        super(Stimulus, self).__init__()
        self.imgIndex = imgI
        self.timeStamp=timeStamp
        


def switchImg(img, panel):
    panel.configure(image=img)
    panel.image = img

def displayImgs(stimuli, panelLeft, panelRight):
    time.sleep(1.0)
    for i in range(len(faceImages)):
        panel=panelLeft
        blankImg=nonTargetBlankImg
        if i%2==0:
            panel=panelRight
            blankImg=TargetBlankImg

        switchImg(faceImages[i], panel)
        stimuli.append(Stimulus(i, time.time()))
        time.sleep(1.0)
        panel.configure(image=blankImg)
        panel.image = blankImg
        
        
def printTimeStamps():
    for i in range(10):
        for s in stimuli:
            print(s.timeStamp)
        time.sleep(2.0)


window = tk.Tk()
faceImages=[]
stimuli=[]


for i in range(maxIndex+1):
    invertImg=ImageTk.PhotoImage(Image.open("faceImg/InvertedFace"+str(i)+".jpg"))
    faceImages.append(invertImg)
    regularImg=ImageTk.PhotoImage(Image.open("faceImg/RegularFace"+str(i)+".jpg"))
    faceImages.append(regularImg)
nonTargetBlankImg=ImageTk.PhotoImage(Image.open("NonTargetBlank.png"))
TargetBlankImg=ImageTk.PhotoImage(Image.open("TargetBlank.png"))

window.title("Face")
window.geometry("850x600")
prompt=tk.Label(text="prompt")
prompt.pack(side="top", fill="none", expand="yes")
panelLeft = tk.Label(window)
panelLeft.pack(side = "left", fill = "none", expand = "yes")
panelLeft.configure(image=nonTargetBlankImg)
panelLeft.image=nonTargetBlankImg

panelRight = tk.Label(window)
panelRight.pack(side = "right", fill = "none", expand = "yes")
panelRight.configure(image=TargetBlankImg)
panelRight.image=TargetBlankImg



displayThread=threading.Thread(target=displayImgs, args=(stimuli, panelLeft, panelRight))
displayThread.start()

printTimeThread=threading.Thread(target=printTimeStamps)
printTimeThread.start()






window.mainloop()





        