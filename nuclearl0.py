import numpy as np
import matplotlib.pyplot as plt 
from scipy.special import spherical_jn
g=40
M=916.6674494
hb=197.3
k1=np.sqrt((2*M)/(hb**2))
def f(x,E):
    return (-1)*(2*M/(hb**2))*(1/(k1*np.sqrt(E)))*(-1)*(g**2)*((k1*np.sqrt(E)*x)**2)*(1/x)*((spherical_jn(1,(k1*np.sqrt(E))*(x)))**2)*(np.exp(-x))
n=10000
a=0.0001
b=100
h=(b-a)/n
for E in range (10,301,10):
    suma=0
    for i in range (1,n):
        Area=f(a+i*h,E)
        suma+=Area
        integral=h*((f(a,E)+f(b,E))/2 +suma)
    print(integral)
     
  

