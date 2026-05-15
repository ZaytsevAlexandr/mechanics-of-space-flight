import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def r2bp(t,y):
    r=y[:3]
    v=y[3:]
    rn=np.linalg.norm(r)
    a=-r/rn**3
    return np.concatenate((v,a))

calls=0

def residue(v0,t0,tf,r0,rf):
    global calls
    calls+=1
    y0=np.concatenate((r0,v0))
    sol=solve_ivp(r2bp,[t0,tf],y0,method='RK45',rtol=1e-10,atol=1e-12)
    r=sol.y[:3,-1]
    return r-rf

def jac(v,t0,tf,r0,rf):
    h=1e-6
    J=np.zeros((3,3))
    for i in range(3):
        vp=v.copy()
        vm=v.copy()
        vp[i]+=h
        vm[i]-=h
        J[:,i]=(residue(vp,t0,tf,r0,rf)-residue(vm,t0,tf,r0,rf))/(2*h)
    return J

r0=np.array([1,0,0],dtype=float)
rf=np.array([0,1.2,0],dtype=float)
t0=0
tf=np.pi/2
v=np.array([0,1,0],dtype=float)

start=time.time()

for i in range(20):
    res=residue(v,t0,tf,r0,rf)
    print(i,calls,np.linalg.norm(res))

    if np.linalg.norm(res)<1e-10:
        break

    J=jac(v,t0,tf,r0,rf)
    dv=np.linalg.solve(J,-res)
    v=v+dv

finish=time.time()

print(v)
print(finish-start)

y0=np.concatenate((r0,v))
t=np.linspace(t0,tf,500)
sol=solve_ivp(r2bp,[t0,tf],y0,method='RK45',t_eval=t,rtol=1e-10,atol=1e-12)

plt.plot(sol.y[0],sol.y[1])
plt.scatter([r0[0],rf[0]],[r0[1],rf[1]])
plt.axis('equal')
plt.grid()
plt.savefig('89result')

# 0 1 0.20000000009630625
# 1 8 0.003961415306264619
# 2 15 2.8464621750804502e-06
# 3 22 1.3215542439807626e-12
# [-0.04082325  1.12021287  0.        ]
# 0.06864500045776367