import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def rhs(t,u):
    y=u[:6]
    p=u[6:].reshape(6,6)
    r=y[:3]
    v=y[3:]
    rn=np.linalg.norm(r)
    a=-r/rn**3
    da=-np.eye(3)/rn**3+3*np.outer(r,r)/rn**5
    A=np.zeros((6,6))
    A[:3,3:]=np.eye(3)
    A[3:,:3]=da
    dp=A@p
    return np.concatenate((v,a,dp.reshape(-1)))

calls=0

def residue_and_jac(v0,t0,tf,r0,rf):
    global calls
    calls+=1
    y0=np.concatenate((r0,v0))
    p0=np.eye(6).reshape(-1)
    u0=np.concatenate((y0,p0))
    sol=solve_ivp(rhs,[t0,tf],u0,method='RK45',rtol=1e-10,atol=1e-12)
    uf=sol.y[:,-1]
    rf_calc=uf[:3]
    p=uf[6:].reshape(6,6)
    return rf_calc-rf,p[:3,3:]

r0=np.array([1,0,0],dtype=float)
rf=np.array([0,1.2,0],dtype=float)
t0=0
tf=np.pi/2
v=np.array([0,1,0],dtype=float)

start=time.time()

for i in range(20):
    res,J=residue_and_jac(v,t0,tf,r0,rf)
    print(i,calls,np.linalg.norm(res))

    if np.linalg.norm(res)<1e-10:
        break

    dv=np.linalg.solve(J,-res)
    v=v+dv

finish=time.time()

print(v)
print(calls)
print(finish-start)

y0=np.concatenate((r0,v))
t=np.linspace(t0,tf,500)
sol=solve_ivp(lambda t,y:rhs(t,np.concatenate((y,np.eye(6).reshape(-1))))[:6],[t0,tf],y0,method='RK45',t_eval=t,rtol=1e-10,atol=1e-12)

plt.plot(sol.y[0],sol.y[1])
plt.scatter([r0[0],rf[0]],[r0[1],rf[1]])
plt.axis('equal')
plt.grid()
plt.savefig('90result')

# 0 1 0.20000000001335738
# 1 2 0.003961415342334798
# 2 3 2.84646370303476e-06
# 3 4 1.3196788943585259e-12
# [-0.04082325  1.12021287  0.        ]
# 4
# 0.045888662338256836