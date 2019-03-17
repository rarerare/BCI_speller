import ast
import matplotlib.pyplot as plt
f=open('signal_data/signal03_16_2019__12_14_30.txt')
strL=f.read()
#print(strL)
l=ast.literal_eval(strL)
print(len(l))
plt.plot([t[2] for t in l])
plt.plot([t[0] for t in l])

plt.show()
