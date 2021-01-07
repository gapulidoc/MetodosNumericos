corrimiento0=open("angulofase.txt","w")
import numpy as np
import matplotlib.pyplot as plt 
from scipy.special import spherical_jn
c=16.35321882
M=916.67
k=0.217
def f(x):
    return c*(20/np.sqrt(20))*(x**2)*(np.exp(-x*M))*((spherical_jn(0,k*x*(np.sqrt(20))))**2)*(1/x)
n=10000
a=0.0001
b=60
h=(b-a)/n
suma=0
for i in range (1,n):
    Area=f(a+i*h)
    suma+=Area

integral=(h*((f(a)+f(b))/2 +suma))
delta=(np.arcsin(integral))*180/(np.pi)
print(delta)
corrimiento0.write(str(delta))
corrimiento0.write("\n") 
corrimiento0.close()

  





