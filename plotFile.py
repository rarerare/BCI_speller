import ast
import matplotlib.pyplot as plt
f=open('signal_data/signal03_08_2019__12_13_19.txt')
strL=f.read()
#print(strL)
l=ast.literal_eval(strL)
print(len(l))
plt.plot([t[0] for t in l])
plt.show()
