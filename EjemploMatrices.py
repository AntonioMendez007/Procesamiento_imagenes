#Matriz de 5 x 5 con todas su propiedades 
import numpy as np
m = np.arange(25).reshape(5,5)

print(m)
print(m.ndim)
print(m.shape)
print(m.size)
print(m.dtype)
print(m.itemsize)

a=np.arange(5)
print('\nOpreaciones basicas')
print(a)
b=a>=3
print(b)
c=a%2 == 0
print(c)

e=np.ones((2,5))
t=np.arange(5)
juntos=np.vstack((e,t))
print(juntos)
#separar=np.hsplit(juntos,(1,3)) almacena 3 arreglos
#de esta manera podemos acceder o asignarle un arreglo a cada variable
(x,y,z)=np.hsplit(juntos,(1,3))

print(x)

