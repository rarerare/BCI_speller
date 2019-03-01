import mindwave
import time
import matplotlib.pyplot as plt
headset = mindwave.Headset('/dev/tty.MindWaveMobile-SerialPo', '625f')
time.sleep(2)

headset.connect()
signal=[]

start_time=time.time()
while True:
    v=headset.raw_value
    time.sleep(0.001)
    print(v)
    signal.append(v)
    if time.time()>start_time+30:
        break

plt.plot(signal)
plt.show()
f=open('signal.txt', 'w')
f.write(str(signal))
f.close()

