import numpy as np
import matplotlib.pyplot as plt 
from scipy.special import spherical_jn
def f(x):
    return (-1)*(40**2)*((30*x)**2)*(1/x)*((spherical_jn(1,30*x))**2)*(np.exp(-x))
n1=10000
a1=0.0001
b1=30
h1=(b1-a1)/n1
suma1=0
for i in range (1,n1):
    Area1=f(a1+i*h1)
    suma1+=Area1
integral1=h1*((f(a1)+f(b1))/2 +suma1)
print(integral1)


def f(x):
    return (-1)*(40**2)*((30*x)**2)*(1/x)*((spherical_jn(2,30*x))**2)*(np.exp(-x))
n=10000
a=0.0001
b=30
h=(b-a)/n
suma=0
for i in range (1,n):
    Area=f(a+i*h)
    suma+=Area
integral=h*((f(a)+f(b))/2 +suma)
print(integral)



def f(x):
    return (-1)*(40**2)*((30*x)**2)*(1/x)*((spherical_jn(3,30*x))**2)*(np.exp(-x))
n=10000
a=0.0001
b=30
h=(b-a)/n
suma=0
for i in range (1,n):
    Area=f(a+i*h)
    suma+=Area
integral=h*((f(a)+f(b))/2 +suma)
print(integral)


print(np.arcsin(0.07))


x=np.arange(0.00001,10,0.0001)
y=(-1)*(40**2)*((30*x)**2)*(1/x)*((spherical_jn(0,30*x))**2)*(np.exp(-x))
plt.plot(x,y)
plt.show()


