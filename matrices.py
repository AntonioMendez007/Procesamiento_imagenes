import numpy as np
# Una matriz es una colección de elementos formados por filas y columnas

a = np.arange(10).reshape(2,5)

v=np.array([(1.5,2,3),(4,5,6)])

print(v)

n=np.empty((2,2))
print(n)


t=np.array([(100,255),(411,255)])
print("-----------")
print(t[0][0])