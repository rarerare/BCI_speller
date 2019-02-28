from PIL import Image, ImageTk
import Tkinter as tk
import threading
from threading import Timer
import time
class Stimulus(object):
    """docstring for stimulus"""
    def __init__(self, img):
        super(Stimulus, self).__init__()
        self.img = img
        self.timeStamp=-1
        
maxIndex=3
interval_stimulus=1

def switchImg(stimulus, panel):
    panel.configure(image=stimulus.img)
    panel.image = stimulus.img
    stimulus.timeStamp=time.time()



imgPath="faceImg/InvertedFace0.jpg"

window = tk.Tk()
faceImages=[]
stimuli=[]
for i in range(maxIndex+1):
    invertImg=ImageTk.PhotoImage(Image.open("faceImg/InvertedFace"+str(i)+".jpg"))
    faceImages.append(invertImg)
    stimuli.append(Stimulus(invertImg))
    regularImg=ImageTk.PhotoImage(Image.open("faceImg/RegularFace"+str(i)+".jpg"))
    faceImages.append(regularImg)
    stimuli.append(Stimulus(regularImg))


window.title("Face")
window.geometry("1000x500")
prompt=tk.Label
panelLeft = tk.Label(window)
panelLeft.pack(side = "left", fill = "none", expand = "no")
panelRight = tk.Label(window)
panelRight.pack(side = "left", fill = "none", expand = "no")
for i in range(len(stimuli)):
    panel=panelLeft
    if i%2==0:
        panel=panelRight

    t = Timer((i+1)*interval_stimulus, switchImg, args=[stimuli[i], panel])

    t.start()

def printTimeStamps():
    for s in stimuli:
        print(s.timeStamp)

t = Timer((2*(maxIndex+2))* interval_stimulus,printTimeStamps)
t.start()



window.mainloop()



        