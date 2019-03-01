from NeuroPy import NeuroPy
object1 = NeuroPy('/dev/tty.MindWaveMobile-SerialPo')
def attention_callback(attention_value): 
#"this function will be called everytime NeuroPy has a new value for attention" 
    print "Value of attention is",attention_value 
#do other stuff (fire a rocket), based on the obtained value of attention_value 
#do some more stuff 
    return None 

#set call back: 
object1.setCallBack("attention",attention_callback) 

#call start method 
object1.start() 


while True: 
    #print(object1.rawValue)
    if(object1.meditation>1): #another way of accessing data provided by headset (1st being call backs) 
        object1.stop()