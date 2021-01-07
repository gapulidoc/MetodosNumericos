archivo2=open("Datos2.txt","w")
import numpy as np
import matplotlib.pyplot as plt 
from scipy.special import spherical_jn
g=40
M=916.6674494
hb=197.3
def f(x,E):
    return (-1)*((2*M)/(hb**2))*(1/(np.sqrt(2*M*E/(hb**2))))*(-1)*(g**2)*((np.sqrt(2*M*E/(hb**2))*x)**2)*(1/x)*(((np.pi/180)*spherical_jn(2,(np.sqrt(2*M*E/(hb**2)))*(x*(np.pi)/180)))**2)*(np.exp(-x))
n=10000
a=0.0001
b=30
h=(b-a)/n
for E in range (10,301,10):
    suma=0
    for i in range (1,n):
        Area=f(a+i*h,E)
        suma+=Area
        integral=h*((f(a,E)+f(b,E))/2 +suma)
        delta=(np.arcsin(integral))*180/(np.pi)
    archivo2.write(str(delta))
    archivo2.write("\n") 
    print(delta)
archivo2.close()   
  

