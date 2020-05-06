from numpy import random
import numpy as np
import matplotlib.pyplot as plt



size = 100000
#1D
r = random.choice([-1,0,1],(size,1))
i = list(range(0,size))
result = r.cumsum(0)
print(result)
plt.plot(i, result)
plt.show()

#2D
r = random.choice([-1,0,1], (size,2))
result = r.cumsum(0)
s = result[:1]
e = result[-1:]
print(result[:,0])

plt.ylim(-500,500)
plt.xlim(-500,500)
plt.plot(s[:,0],s[:,1],c='red', marker='+')
plt.plot(e[:,0],e[:,1],c='red', marker='+')
plt.plot(result[:,0],result[:,1],alpha=0.5,c='blue')
plt.show()



