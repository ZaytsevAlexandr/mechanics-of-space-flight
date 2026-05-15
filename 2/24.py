import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2*np.pi,2*np.pi,1000)

fig,(ax1,ax2)=plt.subplots(2,1)

ax1.plot(x,np.sin(x))
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.grid()

ax2.plot(x,np.cos(x))
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.grid()

plt.savefig('24result')
 