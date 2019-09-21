import numpy as np
import cv2
from matplotlib import pyplot as plt

c,t1 = np.loadtxt('Resultados_Bubble/valores_C++.txt',delimiter = ',',unpack = True)
p,t2 = np.loadtxt('Resultados_Bubble/valores_python.txt',delimiter = ',',unpack = True)
j,t3 = np.loadtxt('Resultados_Bubble/valores_Java.txt',delimiter = ',',unpack = True)
plt.plot(c,t1, color = "blue",label = "C++")
plt.plot(p,t2, color = "green",label = "Python")
plt.plot(j,t3, color = "red",label = "Java")
plt.title('BubbleSort')
plt.xlabel('Numero de Elementos')
plt.ylabel('Tiempo')
plt.legend()
plt.show();
